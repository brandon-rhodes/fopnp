#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - mime_headers.py
# This program requires Python 2.5 or above

from email.mime.text import MIMEText
from email.header import Header

message = """Hello,

This is a test message from Chapter 16.  I hope you enjoy it!

-- Anonymous"""

msg = MIMEText(message)
msg['To'] = 'recipient@example.com'
fromhdr = Header()
fromhdr.append("Michael M\xfcller")
fromhdr.append('<mmueller@example.com>')
msg['From'] = fromhdr
msg['Subject'] = 'Test Message, Chapter 16'

print(msg.as_string())
