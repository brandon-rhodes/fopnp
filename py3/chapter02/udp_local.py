#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_local.py
# UDP client and server on localhost

import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', port))
    print('Listening at {}'.format(s.getsockname()))
    while True:
        data, address = s.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        s.sendto(data, address)

def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'This message was generated at {}'.format(datetime.now())
    data = text.encode('ascii')
    s.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(s.getsockname()))
    data, address = s.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
