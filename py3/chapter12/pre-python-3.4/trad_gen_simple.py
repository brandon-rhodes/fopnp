#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/pre-python-3.4/trad_gen_simple.py
# Traditional Message Generation, Simple

from email.message import Message
text = """Hello,

This is a test message from Chapter 12.  I hope you enjoy it!

-- Anonymous"""

msg = Message()
msg['To'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 12'
msg.set_payload(text)

print(msg.as_string())
