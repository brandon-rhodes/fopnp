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
        """h1 <-> s1 <-> h2 <-> s2 <-> h3"""
        Topo.__init__(self, **opts)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h1 = self.addHost('h1', ip='10.0.1.2/24')
        h2 = self.addHost('h2', ip='10.0.1.1/24')
        h3 = self.addHost('h3', ip='10.0.2.2/24')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s2)

def main(do_interactive):
    topo = RoutedTopo()
    net = Mininet(topo, controller=OVSController)
    net.start()
    net['h2'].cmd('ip addr add 10.0.2.1/24 dev h2-eth1')
    net['h1'].cmd('route add default gw 10.0.1.1')
    net['h3'].cmd('route add default gw 10.0.2.1')
    net['h2'].cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    print "Host connections:"
    dumpNodeConnections(net.hosts)
    if do_interactive:
        hosts = ['h1', 'h2', 'h3']
        for host in hosts:
            net[host].cmd('dnsmasq --interface=lo --no-dhcp-interface=lo'
                          ' --no-daemon --no-resolv --no-hosts'
                          ' --addn-hosts=/home/brandon/fopnp/playground/hosts &')
        net.terms += makeTerms(net.hosts, 'host')
        CLI(net)
        for host in hosts:
            net[host].cmd('kill %dnsmasq')
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
