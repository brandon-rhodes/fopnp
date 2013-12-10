#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 15 - open_imap.py
# Opening an IMAP connection with the powerful IMAPClient

import getpass, sys
from imapclient import IMAPClient

try:
    hostname, username = sys.argv[1:]
except ValueError:
    print 'usage: %s hostname username' % sys.argv[0]
    sys.exit(2)

c = IMAPClient(hostname, ssl=True)
try:
    c.login(username, getpass.getpass())
except c.Error, e:
    print 'Could not log in:', e
    sys.exit(1)

print 'Capabilities:', c.capabilities()
print 'Listing mailboxes:'
data = c.list_folders()
for flags, delimiter, folder_name in data:
    print '  %-30s%s %s' % (' '.join(flags), delimiter, folder_name)
c.logout()
