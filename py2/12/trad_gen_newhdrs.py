#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 12 - trad_gen_newhdrs.py
# Traditional Message Generation with Date and Message-ID
# This program requires Python 2.5 or above

import email.utils
from email.message import Message

message = """Hello,

This is a test message from Chapter 12.  I hope you enjoy it!

-- Anonymous"""

msg = Message()
msg['To'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 12'
msg['Date'] = email.utils.formatdate(localtime = 1)
msg['Message-ID'] = email.utils.make_msgid()
msg.set_payload(message)

print msg.as_string()
