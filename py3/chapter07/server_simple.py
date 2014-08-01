#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/server_simple.py
# Simple server that only serves one client at a time; others have to wait.

import zen_example

def server(listener):
    while True:
        sock, sockname = listener.accept()
        zen_example.handle_client_conversation(sock)

if __name__ == '__main__':
    listener = zen_example.create_server_socket('simple server')
    server(listener)
