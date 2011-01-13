#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 12 - mime_headers.py

from email.mime.text import MIMEText
from email.header import Header

message = """Hello,

This is a test message from Chapter 12.  I hope you enjoy it!

-- Anonymous"""

msg = MIMEText(message)
msg['To'] = 'recipient@example.com'
fromhdr = Header()
fromhdr.append('Michael Müller', 'iso-8859-1')  # 'utf-8' is even more general
fromhdr.append('<mmueller@example.com>')
msg['From'] = fromhdr
msg['Subject'] = 'Test Message, Chapter 12'

print(msg.as_string())
