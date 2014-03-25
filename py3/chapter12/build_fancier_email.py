#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/build_fancier_email.py

import email.utils
from email.message import EmailMessage

message = """Hello,

This is a test message from Chapter 12.

 - Anonymous"""

def main():
    msg = EmailMessage()
    msg['To'] = 'recipient@example.com'
    msg['From'] = 'Test Sender <sender@example.com>'
    msg['Subject'] = 'Test Message, Chapter 12'
    msg['Date'] = email.utils.formatdate(localtime=True)
    msg['Message-ID'] = email.utils.make_msgid()
    msg.set_content(message)
    print(msg.as_string())

if __name__ == '__main__':
    main()
