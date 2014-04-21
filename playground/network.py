#!/usr/bin/python2
#
# Note the shebang line above: this script is hard-wired to use Python 2
# in Ubuntu's native /usr/bin/ because that is the interpreter which is
# guaranteed access to the `mininet` library after `install.sh` has run.

import argparse
import os
import sys
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet, makeTerms
from mininet.node import OVSController
from mininet.topo import Topo
from mininet.util import dumpNodeConnections

this_dir = os.path.dirname(os.path.abspath(__file__))

class RoutedTopo(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)

        backbone = self.addHost('backbone', ip='10.1.1.1/32')

        # The ISP and its customers.

        isp = self.addHost('isp', ip='10.25.1.1/32')
        self.addLink(isp, backbone)

        modemA = self.addHost('modemA', ip='10.25.1.65/24')
        modemB = self.addHost('modemB', ip='10.25.1.66/24')

        h1 = self.addHost('h1', ip='192.168.1.11/24')
        h2 = self.addHost('h2', ip='192.168.1.12/24')
        h3 = self.addHost('h3', ip='192.168.1.13/24')

        h4 = self.addHost('h4', ip='192.168.1.11/24')

        self.addLink(modemA, isp)
        self.addLink(modemB, isp)

        sA = self.addSwitch('s1')
        sB = self.addSwitch('s2')

        self.addLink(modemA, sA)
        self.addLink(h1, sA)
        self.addLink(h2, sA)
        self.addLink(h3, sA)

        self.addLink(modemB, sB)
        self.addLink(h4, sB)

        # The example.com corporation.

        example = self.addHost('example', ip='10.130.1.1/32')
        self.addLink(backbone, example)

        ftp = self.addHost('ftp', ip='10.130.1.2/24')
        mail = self.addHost('mail', ip='10.130.1.3/24')
        www = self.addHost('www', ip='10.130.1.4/24')

        s3 = self.addSwitch('s3')

        self.addLink(example, s3)
        self.addLink(ftp, s3)
        self.addLink(mail, s3)
        self.addLink(www, s3)

def configure_network(net):
    hosts = 'h1', 'h2', 'h3', 'h4'
    modems = 'modemA', 'modemB'
    gateways = 'isp', 'backbone', 'example'
    servers = 'ftp', 'mail', 'www'

    for host in hosts:
        net[host].cmd('ip route add default via 192.168.1.1')

    for modem in modems:
        net[modem].cmd('ip addr add 192.168.1.1/24 dev %s-eth1' % modem)
        net[modem].cmd('ip route add default via 10.25.1.1')
        net[modem].cmd('iptables --table nat --append POSTROUTING'
                       ' --out-interface %s-eth0 -j MASQUERADE' % modem)

    net['isp'].cmd('ip addr add 10.25.1.1/32 dev isp-eth1')
    net['isp'].cmd('ip addr add 10.25.1.1/32 dev isp-eth2')

    net['isp'].cmd('ip route add 10.1.1.1/32 dev isp-eth0')
    net['isp'].cmd('ip route add 10.25.1.65/32 dev isp-eth1')
    net['isp'].cmd('ip route add 10.25.1.66/32 dev isp-eth2')
    net['isp'].cmd('ip route add default via 10.1.1.1')

    net['backbone'].cmd('ip addr add 10.1.1.1/32 dev backbone-eth1')

    net['backbone'].cmd('ip route add 10.25.1.1/32 dev backbone-eth0')
    net['backbone'].cmd('ip route add 10.25.0.0/16 via 10.25.1.1')

    net['backbone'].cmd('ip route add 10.130.1.1/32 dev backbone-eth1')
    net['backbone'].cmd('ip route add 10.130.1.0/24 via 10.130.1.1')

    net['example'].cmd('ip addr add 10.130.1.1/24 dev example-eth1')

    net['example'].cmd('ip route add 10.1.1.1/32 dev example-eth0')
    net['example'].cmd('ip route add default via 10.1.1.1')

    for server in servers:
        net[server].cmd('ip route add default via 10.130.1.1')

    for gateway in gateways + modems:
        net[gateway].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

def start_dns(net):
    """Start dnsmasq on every server.

    Since all network programs share the parent host's /etc/resolv.conf
    which, per Ubuntu practice, points at localhost, we simply provide
    each host with its own loopback-bound copy of dnsmasq that is hard
    coded to serve up IPs from our custom hosts file.  Works great.

    """
    for host in net.hosts:
        host.cmd('dnsmasq --interface=lo --no-dhcp-interface=lo'
                 ' --no-daemon --no-resolv --no-hosts'
                 ' --addn-hosts=../services/hosts &')
        host.cleanup_commands.append('kill %?dnsmasq')

def start_dovecot(net):
    net['mail'].cmd('python3 ../services/custom_dovecot.py'
                    ' >log.dovecot 2>&1 &')
    net['mail'].cleanup_commands.append('kill %?custom_dovecot')

def start_httpd(net):
    net['www'].cmd('python3 ../services/custom_httpd.py ../certs/www.pem'
                   ' >log.httpd 2>&1 &')
    net['www'].cleanup_commands.append('kill %?custom_httpd')

def start_smtpd(net):
    net['mail'].cmd('python3 ../services/custom_smtpd.py'
                    ' >log.smtpd 2>&1 &')
    net['mail'].cleanup_commands.append('kill %?custom_smtpd')

def start_services(net):
    for host in net.hosts:
        host.cmd('umask 022')
        host.cmd('cd %s/var' % this_dir)
        host.cleanup_commands = []
    start_dns(net)
    start_dovecot(net)
    start_httpd(net)
    start_smtpd(net)

def main(args):
    topo = RoutedTopo()
    net = Mininet(topo, controller=OVSController)
    net.start()
    try:
        configure_network(net)
        print("Host connections:")
        dumpNodeConnections(net.hosts)
        if args.p:
            net.pingAll()
        if args.i or args.s:
            start_services(net)
        if args.s:
            net['h1'].cmd(this_dir + '/run_session.sh')
        if args.i:
            hosts = [net[hostname] for hostname in args.host]
            net.terms += makeTerms(hosts, 'host')  # net.hosts
            CLI(net)
    finally:
        try:
            for host in net.hosts:
                for command in getattr(host, 'cleanup_commands', ()):
                    try:
                        host.cmd(command)
                    except:
                        print >>sys.stderr, ('Error on %s: %r'
                                             % (host.name, command))
        finally:
            net.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='The Foundations of Python Network Programming'
        ' Mininet playground')
    parser.add_argument('host', nargs='*', help='hosts for which xterms'
                        ' will be automatically started in "-i" mode'
                        ' (defaults to "h1")')
    parser.add_argument('-i', action='store_true', help='build network then'
                        ' go interactive, with CLI and xterms')
    parser.add_argument('-p', action='store_true', help='build network then'
                        ' run ping test between all hosts')
    parser.add_argument('-s', action='store_true', help='build network then'
                        ' re-run py3/session.txt on host "h1"')
    args = parser.parse_args()
    if not (args.i or args.p or args.s):
        parser.print_help()
        parser.exit(2)
    if not args.host:
        args.host = ['h1']
    setLogLevel('info')
    try:
        main(args)
    except KeyboardInterrupt:
        pass
