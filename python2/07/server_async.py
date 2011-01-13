#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - server_async.py
# Using the ancient "asyncore" framework to write a server.

import asyncore, asynchat, lancelot

class LancelotRequestHandler(asynchat.async_chat):

    def __init__(self, sock):
        asynchat.async_chat.__init__(self, sock)
        self.set_terminator('?')
        self.data = ''

    def collect_incoming_data(self, more_data):
        self.data += more_data

    def found_terminator(self):
        answer = dict(lancelot.qa)[self.data + '?']
        self.push(answer)
        self.initiate_send()
        self.data = ''

class LancelotServer(asyncore.dispatcher):
    def handle_accept(self):
        sock, address = self.accept()
        LancelotRequestHandler(sock)

sock = lancelot.setup()
ls = LancelotServer(sock)
ls.accepting = True  # since we already called listen()
asyncore.loop()
