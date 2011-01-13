#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - server_twisted.py
# Using Twisted to serve Lancelot users.

from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor
import lancelot

class Lancelot(Protocol):
    def connectionMade(self):
        self.question = ''

    def dataReceived(self, data):
        self.question += data
        if self.question.endswith('?'):
            self.transport.write(dict(lancelot.qa)[self.question])
            self.question = ''

factory = ServerFactory()
factory.protocol = Lancelot
reactor.listenTCP(1060, factory)
reactor.run()
