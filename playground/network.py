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

        isp = self.addHost('isp', ip='10.25.1.1/16')
        modemA = self.addHost('modemA', ip='10.25.1.65/16')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        h1 = self.addHost('h1', ip='192.168.1.11/24')
        h2 = self.addHost('h2', ip='192.168.1.12/24')
        h3 = self.addHost('h3', ip='192.168.1.13/24')

        h4 = self.addHost('h4', ip='192.168.1.11/24')

        self.addLink(modemA, isp)
        self.addLink(modemA, s1)
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

        self.addLink(h4, s2)


        return
        s3 = self.addSwitch('s3')

        modemB = self.addHost('modemB', ip='10.50.1.66/16')

        backbone = self.addHost('backbone', ip='10.1.1.1/8')

        example = self.addHost('example.com', ip='10.130.1.1/24')

        ftp = self.addHost('ftp', ip='10.130.1.2/24')
        mail = self.addHost('mail', ip='10.130.1.3/24')
        www = self.addHost('www', ip='10.130.1.4/24')

        self.addLink(backbone, isp)
        self.addLink(isp, modemA)
        self.addLink(isp, modemB)
        self.addLink(modemB, s2)



        self.addLink(backbone, example)
        self.addLink(example, s3)
        self.addLink(ftp, s3, ftp)
        self.addLink(mail, s3)
        self.addLink(www, s3)

def main(do_interactive):
    hosts = 'h1', #'h2', 'h3', 'h4'
    modems = 'modemA', #'modemB'
    gateways = 'isp', 'backbone', 'example.com'

    topo = RoutedTopo()
    net = Mininet(topo, controller=OVSController)
    net.start()

    for host in hosts:
        net[host].cmd('route add default gw 192.168.1.1')

    for modem in modems:
        net[modem].cmd('ip addr add 192.168.1.1/24 dev %s-eth1' % modem)
        net[modem].cmd('route add default gw 10.25.1.1')
        net[modem].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
        net[modem].cmd('iptables --table nat --append POSTROUTING'
                       ' --out-interface %s-eth0 -j MASQUERADE' % modem)


    # for name in hosts + modems + gateways:
    #     net[host].cmd('dnsmasq --interface=lo --no-dhcp-interface=lo'
    #                   ' --no-daemon --no-resolv --no-hosts'
    #                   ' --addn-hosts=/home/brandon/fopnp/playground/hosts &')

    #net['isp'].cmd('ip

    #net['h2'].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    print "Host connections:"
    dumpNodeConnections(net.hosts)
    if do_interactive:
        hosts = [net['h1'], net['modemA']]
        net.terms += makeTerms(hosts, 'host')  # net.hosts
        CLI(net)
        # for host in hosts:
        #     host.cmd('kill %dnsmasq')
    else:
        net.pingAll()
    net.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple Mininet with a router')
    parser.add_argument('-i', action='store_true',
                        help='run interactively with xterms and a cli')
    args = parser.parse_args()
    setLogLevel('info')
    main(args.i)
