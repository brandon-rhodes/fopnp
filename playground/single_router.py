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
        h1 = self.addHost('h1', ip=None)
        h2 = self.addHost('h2', ip=None)
        h3 = self.addHost('h3', ip=None)
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s2)
        # print self[h2]
        # print dir(h2)
        # h2.cmd('ip addr add 10.0.2.1/24 dev h2-eth1')

def main():
    topo = RoutedTopo()
    net = Mininet(topo, controller=OVSController)
    net.start()
    net['h1'].cmd('ip addr add 10.0.1.2/24 dev h1-eth0')
    net['h2'].cmd('ip addr add 10.0.1.1/24 dev h2-eth0')
    net['h2'].cmd('ip addr add 10.0.2.1/24 dev h2-eth1')
    net['h3'].cmd('ip addr add 10.0.2.2/24 dev h3-eth0')
    print "Host connections:"
    dumpNodeConnections(net.hosts)
    net.terms += makeTerms(net.hosts, 'host')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main()
