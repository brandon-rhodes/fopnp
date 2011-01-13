#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 12 - trad_gen_simple.py
# Traditional Message Generation, Simple
# This program requires Python 2.5 or above

from email.message import Message
text = """Hello,

This is a test message from Chapter 12.  I hope you enjoy it!

-- Anonymous"""

msg = Message()
msg['To'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 12'
msg.set_payload(text)

print msg.as_string()
