#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 4 - dns_mx.py
# Looking up a mail domain - the part of an email address after the `@`

import sys, DNS

if len(sys.argv) != 2:
    print >>sys.stderr, 'usage: dns_basic.py <hostname>'
    sys.exit(2)

def resolve_hostname(hostname, indent=0):
    """Print an A or AAAA record for `hostname`; follow CNAMEs if necessary."""
    indent = indent + 4
    istr = ' ' * indent
    request = DNS.Request()
    reply = request.req(name=sys.argv[1], qtype=DNS.Type.A)
    if reply.answers:
        for answer in reply.answers:
            print istr, 'Hostname', hostname, '= A', answer['data']
        return
    reply = request.req(name=sys.argv[1], qtype=DNS.Type.AAAA)
    if reply.answers:
        for answer in reply.answers:
            print istr, 'Hostname', hostname, '= AAAA', answer['data']
        return
    reply = request.req(name=sys.argv[1], qtype=DNS.Type.CNAME)
    if reply.answers:
        cname = reply.answers[0]['data']
        print istr, 'Hostname', hostname, 'is an alias for', cname
        resolve_hostname(cname, indent)
        return
    print istr, 'ERROR: no records for', hostname

def resolve_email_domain(domain):
    """Print mail server IP addresses for an email address @ `domain`."""
    request = DNS.Request()
    reply = request.req(name=sys.argv[1], qtype=DNS.Type.MX)
    if reply.answers:
        print 'The domain %r has explicit MX records!' % (domain,)
        print 'Try the servers in this order:'
        datalist = [ answer['data'] for answer in reply.answers ]
        datalist.sort()  # lower-priority integers go first
        for data in datalist:
            priority = data[0]
            hostname = data[1]
            print 'Priority:', priority, '  Hostname:', hostname
            resolve_hostname(hostname)
    else:
        print 'Drat, this domain has no explicit MX records'
        print 'We will have to try resolving it as an A, AAAA, or CNAME'
        resolve_hostname(domain)

DNS.DiscoverNameServers()
resolve_email_domain(sys.argv[1])
