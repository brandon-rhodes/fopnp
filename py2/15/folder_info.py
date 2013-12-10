#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 15 - folder_info.py
# Opening an IMAP connection with IMAPClient and listing folder information.

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
else:
    select_dict = c.select_folder('INBOX', readonly=True)
    for k, v in select_dict.items():
        print '%s: %r' % (k, v)
    c.logout()
