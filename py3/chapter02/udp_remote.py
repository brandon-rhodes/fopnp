#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 2 - udp_remote.py
# UDP client and server for talking over the network

import random, socket, sys

MAX_BYTES = 65535
PORT = 1060

def server(interface):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((interface, PORT))
    print('Listening at', s.getsockname())
    while True:
        data, address = s.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            text = data.decode('ascii')
            print('The client at {} says {!r}'.format(address, text))
            message = 'Your data was {} bytes long'.format(data)
            s.sendto(message.encode('ascii'), address)
        else:
            print('Pretending to drop packet from {}'.format(address))

def client(hostname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    s.connect((hostname, PORT))
    print('Client socket name is {}'.format(s.getsockname()))

    delay = 0.1
    while True:
        s.send(b'This is another message')
        print('Waiting up to {} seconds for a reply'.format(delay))
        s.settimeout(delay)
        try:
            data = s.recv(MAX_BYTES)
        except socket.timeout:
            delay *= 2  # wait even longer for the next request
            if delay > 2.0:
                raise RuntimeError('I think the server is down')
        else:
            break   # we are done, and can stop looping

    print('The server says {!r}'.format(data))

if __name__ == '__main__':
    if 2 <= len(sys.argv) <= 3 and sys.argv[1] == 'server':
        interface = (sys.argv[2] if len(sys.argv) > 2 else '')
        server(interface)
    elif len(sys.argv) == 3 and sys.argv[1] == 'client':
        hostname = sys.argv[2]
        client(hostname)
    else:
        print('usage: udp_remote.py server [<interface>]', file=sys.stderr)
        print('   or: udp_remote.py client <host>', file=sys.stderr)
        sys.exit(2)
