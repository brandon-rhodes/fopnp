#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 2 - udp_local.py
# UDP client and server on localhost

import socket, sys
from datetime import datetime

MAX_BYTES = 65535
PORT = 1060

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', PORT))
    print('Listening at {}'.format(s.getsockname()))
    while True:
        data, address = s.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        s.sendto(data, address)

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'This message was generated at {}'.format(datetime.now())
    data = text.encode('ascii')
    s.sendto(data, ('127.0.0.1', PORT))
    print('The OS assigned me the address {}'.format(s.getsockname()))
    data, address = s.recvfrom(MAX_BYTES)  # Danger! See Chapter 2
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))

if __name__ == '__main__':
    if sys.argv[1:] == ['server']:
        server()
    elif sys.argv[1:] == ['client']:
        client()
    else:
        print('usage: udp_local.py (server|client)', file=sys.stderr)
