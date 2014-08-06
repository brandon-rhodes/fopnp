#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/server_simple.py
# Simple server that only serves one client at a time; others have to wait.

import zen_example

if __name__ == '__main__':
    address = zen_example.parse_command_line('simple server')
    listener = zen_example.create_server_socket(address)
    zen_example.accept_connections_forever(listener)
