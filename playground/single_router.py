#!/usr/bin/python

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
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s2)

def main():
    topo = RoutedTopo()
    net = Mininet(topo, controller=OVSController)
    net.start()
    print "Host connections:"
    dumpNodeConnections(net.hosts)
    net.terms += makeTerms(net.hosts, 'host')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main()
