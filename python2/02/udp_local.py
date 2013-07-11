#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - udp_local.py
# UDP client and server on localhost

import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

BUFSIZE = 65535
PORT = 1060

if sys.argv[1:] == ['server']:
    s.bind(('127.0.0.1', PORT))
    print 'Listening at', s.getsockname()
    while True:
        data, address = s.recvfrom(BUFSIZE)
        print 'The client at', address, 'says', repr(data)
        s.sendto('Your data was %d bytes' % len(data), address)

elif sys.argv[1:] == ['client']:
    s.sendto('This is my message', ('127.0.0.1', PORT))
    print 'Address after sending', s.getsockname()
    data, address = s.recvfrom(BUFSIZE)  # overly promiscuous - see Chapter 2
    print 'The server', address, 'says', repr(data)

else:
    print >>sys.stderr, 'usage: udp_local.py server|client'
