#!/usr/bin/env python
# POP mailbox downloader with deletion - Chapter 14
# download-and-delete.py

import email, getpass, poplib, sys

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
    response, listings, octets = p.list()
    for listing in listings:
        number, size = listing.split()
        print 'Message', number, '(size is', size, 'bytes):'
        print
        response, lines, octets = p.top(number, 0)
        message = email.message_from_string('\n'.join(lines))
        for header in 'From', 'To', 'Subject', 'Date':
            if header in message:
                print header + ':', message[header]
        print
        print 'Read this message [ny]?'
        answer = raw_input()
        if answer.lower().startswith('y'):
            response, lines, octets = p.retr(number)
            message = email.message_from_string('\n'.join(lines))
            print '-' * 72
            for part in message.walk():
                if part.get_content_type() == 'text/plain':
                    print part.get_payload()
                    print '-' * 72
        print
        print 'Delete this message [ny]?'
        answer = raw_input()
        if answer.lower().startswith('y'):
            p.dele(number)
            print 'Deleted.'
finally:
    p.quit()
