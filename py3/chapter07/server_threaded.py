#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/server_multi.py
# Using multiple threads or processes to serve several clients in parallel.

import zen_example
from threading import Thread

def server(listener, workers=4):
    t = (listener,)
    for i in range(workers):
        Thread(target=zen_example.accept_connections_forever, args=t).start()

if __name__ == '__main__':
    address = zen_example.parse_command_line('simple server')
    listener = zen_example.create_server_socket(address)
    server(listener)
