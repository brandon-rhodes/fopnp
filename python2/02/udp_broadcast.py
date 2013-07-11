#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - udp_broadcast.py
# UDP client and server for broadcast messages on a local LAN

import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

BUFSIZE = 65535
PORT = 1060

if 2 <= len(sys.argv) <= 3 and sys.argv[1] == 'server':
    s.bind(('', PORT))
    print 'Listening for broadcasts at', s.getsockname()
    while True:
        data, address = s.recvfrom(BUFSIZE)
        print 'The client at %r says: %r' % (address, data)

elif len(sys.argv) == 3 and sys.argv[1] == 'client':
    network = sys.argv[2]
    s.sendto('Broadcast message!', (network, PORT))

else:
    print >>sys.stderr, 'usage: udp_broadcast.py server'
    print >>sys.stderr, '   or: udp_broadcast.py client <host>'
    sys.exit(2)
