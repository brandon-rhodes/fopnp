#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - big_sender.py
# Send a big UDP packet to our server.

import IN, socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

PORT = 1060

if len(sys.argv) != 2:
    print >>sys.stderr, 'usage: big_sender.py host'
    sys.exit(2)

hostname = sys.argv[1]
s.connect((hostname, PORT))
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
try:
    s.send('#' * 65000)
except socket.error:
    print 'The message did not make it'
    option = getattr(IN, 'IP_MTU', 14)  # constant taken from <linux/in.h>
    print 'MTU:', s.getsockopt(socket.IPPROTO_IP, option)
else:
    print 'The big message was sent! Your network supports really big packets!'
