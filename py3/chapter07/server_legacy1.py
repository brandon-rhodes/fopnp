#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/server_legacy1.py
# Answering Lancelot requests with a legacy SocketServer.

from socketserver import ThreadingMixIn, TCPServer, BaseRequestHandler
import socket, zen_example

class ZenHandler(BaseRequestHandler):
    def handle(self):
        zen_example.handle_client_conversation(self.request)

class ZenServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1
    # address_family = socket.AF_INET6  # if you need IPv6

if __name__ == '__main__':
    address = zen_example.parse_command_line('legacy SocketServer server')
    server = ZenServer(address, ZenHandler)
    server.serve_forever()
