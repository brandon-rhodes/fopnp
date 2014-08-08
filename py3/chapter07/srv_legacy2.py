#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/srv_legacy2.py
# Uses the legacy "asyncore" Standard Library module to write a server.

import asyncore, asynchat, zen_utils

class ZenRequestHandler(asynchat.async_chat):

    def __init__(self, sock):
        asynchat.async_chat.__init__(self, sock)
        self.set_terminator(b'?')
        self.data = b''

    def collect_incoming_data(self, more_data):
        self.data += more_data

    def found_terminator(self):
        answer = zen_utils.get_answer(self.data + b'?')
        self.push(answer)
        self.initiate_send()
        self.data = b''

class ZenServer(asyncore.dispatcher):

    def handle_accept(self):
        sock, address = self.accept()
        ZenRequestHandler(sock)

if __name__ == '__main__':
    address = zen_utils.parse_command_line('legacy "asyncore" server')
    listener = zen_utils.create_srv_socket(address)
    server = ZenServer(listener)
    server.accepting = True  # we already called listen()
    asyncore.loop()
