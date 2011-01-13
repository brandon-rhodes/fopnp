#!/usr/bin/env python
# POP mailbox scanning - Chapter 14 - mailbox.py

import getpass, poplib, sys

if len(sys.argv) != 3:
    print 'usage: %s hostname user' % sys.argv[0]
    exit(2)

hostname, user = sys.argv[1:]
passwd = getpass.getpass()

p = poplib.POP3_SSL(hostname)
try:
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto, e:
    print "Login failed:", e
else:
    response, listings, octet_count = p.list()
    for listing in listings:
        number, size = listing.split()
        print "Message %s has %s bytes" % (number, size)
finally:
    p.quit()
