#!/usr/bin/python

import argparse
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet, makeTerms
from mininet.node import OVSController
from mininet.topo import Topo
from mininet.util import dumpNodeConnections

class RoutedTopo(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)

        # The ISP and its customers.

        isp = self.addHost('isp', ip='10.25.1.1/16')
        modemA = self.addHost('modemA', ip='10.25.1.65/16')
        modemB = self.addHost('modemB', ip='10.25.1.66/16')

        h1 = self.addHost('h1', ip='192.168.1.11/24')
        h2 = self.addHost('h2', ip='192.168.1.12/24')
        h3 = self.addHost('h3', ip='192.168.1.13/24')

        h4 = self.addHost('h4', ip='192.168.1.11/24')

        self.addLink(modemB, isp)
        self.addLink(modemA, isp)

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(modemA, s1)
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

        self.addLink(modemB, s2)
        self.addLink(h4, s2)

        # The example.com corporation.

        example = self.addHost('example.com', ip='10.130.1.1/24')

        return
        ftp = self.addHost('ftp', ip='10.130.1.2/24')
        mail = self.addHost('mail', ip='10.130.1.3/24')
        www = self.addHost('www', ip='10.130.1.4/24')

        s3 = self.addSwitch('s3')

        self.addLink(example, s3)
        self.addLink(ftp, s3)
        self.addLink(mail, s3)
        self.addLink(www, s3)

        # The Internet backbone.

        backbone = self.addHost('backbone', ip='10.1.1.1/8')
        self.addLink(backbone, isp)
        self.addLink(backbone, example)

def configure_network(net):
    hosts = 'h1', 'h2', 'h3', 'h4'
    modems = 'modemA', 'modemB'
    gateways = 'isp', 'backbone', 'example.com'
    servers = ()#'ftp', 'mail', 'www'

    for host in hosts:
        net[host].cmd('route add default gw 192.168.1.1')

    for modem in modems:
        net[modem].cmd('ip addr add 192.168.1.1/24 dev %s-eth1' % modem)
        net[modem].cmd('route add default gw 10.25.1.1')
        net[modem].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
        net[modem].cmd('iptables --table nat --append POSTROUTING'
                       ' --out-interface %s-eth0 -j MASQUERADE' % modem)

    for server in servers:
        net[host].cmd('route add default gw 10.130.1.1')

    # for gateway in gateways:
    #     net[gateway].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

def main(do_interactive):
    topo = RoutedTopo()
    net = Mininet(topo, controller=OVSController)
    net.start()
    try:
        configure_network(net)
        print "Host connections:"
        dumpNodeConnections(net.hosts)
        if do_interactive:
            hosts = [net['h1'], net['h4']]
            net.terms += makeTerms(hosts, 'host')  # net.hosts
            CLI(net)
            # for host in hosts:
            #     host.cmd('kill %dnsmasq')
        else:
            net.pingAll()
    finally:
        net.stop()

    # for name in hosts + modems + gateways:
    #     net[host].cmd('dnsmasq --interface=lo --no-dhcp-interface=lo'
    #                   ' --no-daemon --no-resolv --no-hosts'
    #                   ' --addn-hosts=/home/brandon/fopnp/playground/hosts &')

    #net['isp'].cmd('ip
    #net['h2'].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple Mininet with a router')
    parser.add_argument('-i', action='store_true',
                        help='run interactively with xterms and a cli')
    args = parser.parse_args()
    setLogLevel('info')
    main(args.i)
