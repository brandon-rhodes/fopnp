#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/zen.py
# Constants and routines for supporting a certain network conversation.

import argparse, socket

proverbs = {'Beautiful is better than?': 'Ugly.',
            'Explicit is better than?': 'Implicit.',
            'Simple is better than?': 'Complex.'}

def create_server_socket(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(64)
    print('Listening at {}:{}'.format(args.host, args.p))
    return sock

def recv_until(sock, suffix):
    message = b''
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise EOFError('socket closed before we saw {!r}'.format(suffix))
        message += data
    return message
