#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/pre-python-3.4/mime_headers.py

from email.mime.text import MIMEText
from email.header import Header

message_text = """Hello,

This is a test message from Chapter 12.  I hope you enjoy it!

-- Anonymous"""

message = MIMEText(message_text)
message['To'] = 'recipient@example.com'
header = Header()
header.append('Michael Müller', 'iso-8859-1')  # 'utf-8' is even more general
header.append('<mmueller@example.com>')
message['From'] = header
message['Subject'] = 'Test Message, Chapter 12'

print(message.as_string())
