#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 2 - udp_broadcast.py
# UDP client and server for broadcast messages on a local LAN

import socket, sys

BUFSIZE = 65535
PORT = 1060

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', PORT))
    print('Listening for datagrams at {}'.format(s.getsockname()))
    while True:
        data, address = s.recvfrom(BUFSIZE)
        text = data.decode('ascii')
        print('The client at {} says: {!r}'.format(address, text))

def client(network):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    text = 'Broadcast datagram!'
    s.sendto(text.encode('ascii'), (network, PORT))

if __name__ == '__main__':
    if sys.argv[1:] == ['server']:
        server()
    elif len(sys.argv) == 3 and sys.argv[1] == 'client':
        client(sys.argv[2])
    else:
        print('usage: udp_broadcast.py server', file=sys.stderr)
        print('   or: udp_broadcast.py client <network>', file=sys.stderr)
        sys.exit(2)
