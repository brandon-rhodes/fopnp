#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 15 - mailbox_summary.py
# Opening an IMAP connection with IMAPClient and retrieving mailbox messages.

import email, getpass, sys
from imapclient import IMAPClient

try:
    hostname, username, foldername = sys.argv[1:]
except ValueError:
    print 'usage: %s hostname username folder' % sys.argv[0]
    sys.exit(2)

c = IMAPClient(hostname, ssl=True)
try:
    c.login(username, getpass.getpass())
except c.Error, e:
    print 'Could not log in:', e
    sys.exit(1)

c.select_folder(foldername, readonly=True)
msgdict = c.fetch('1:*', ['BODY.PEEK[]'])
for message_id, message in msgdict.items():
    e = email.message_from_string(message['BODY[]'])
    print message_id, e['From']
    payload = e.get_payload()
    if isinstance(payload, list):
        part_content_types = [ part.get_content_type() for part in payload ]
        print '  Parts:', ' '.join(part_content_types)
    else:
        print '  ', ' '.join(payload[:60].split()), '...'

c.logout()
