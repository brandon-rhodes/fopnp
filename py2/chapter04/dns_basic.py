#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 4 - dns_basic.py
# Basic DNS query

import sys, DNS

if len(sys.argv) != 2:
    print >>sys.stderr, 'usage: dns_basic.py <hostname>'
    sys.exit(2)

DNS.DiscoverNameServers()
request = DNS.Request()
for qt in DNS.Type.A, DNS.Type.AAAA, DNS.Type.CNAME, DNS.Type.MX, DNS.Type.NS:
    reply = request.req(name=sys.argv[1], qtype=qt)
    for answer in reply.answers:
        print answer['name'], answer['classstr'], answer['typename'], \
            repr(answer['data'])
