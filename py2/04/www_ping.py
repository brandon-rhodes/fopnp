#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 4 - www_ping.py
# Find the WWW service of an arbitrary host using getaddrinfo().

import socket, sys

if len(sys.argv) != 2:
    print >>sys.stderr, 'usage: www_ping.py <hostname_or_ip>'
    sys.exit(2)

hostname_or_ip = sys.argv[1]

try:
    infolist = socket.getaddrinfo(
        hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
        socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,
        )
except socket.gaierror, e:
    print 'Name service failure:', e.args[1]
    sys.exit(1)

info = infolist[0]  # per standard recommendation, try the first one
socket_args = info[0:3]
address = info[4]
s = socket.socket(*socket_args)
try:
    s.connect(address)
except socket.error, e:
    print 'Network failure:', e.args[1]
else:
    print 'Success: host', info[3], 'is listening on port 80'
