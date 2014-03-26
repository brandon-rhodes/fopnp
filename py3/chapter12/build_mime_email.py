#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/build_fancier_email.py

import email.message, email.utils

text = """Hello,

This is a test message from Chapter 12.

 - Anonymous"""

def main():
    message = email.message.EmailMessage()
    message['To'] = 'recipient@example.com'
    message['From'] = 'Test Sender <sender@example.com>'
    message['Subject'] = 'Test Message, Chapter 12'
    message['Date'] = email.utils.formatdate(localtime=True)
    message['Message-ID'] = email.utils.make_msgid()
    message.set_content(text)
    print(message.as_string())

if __name__ == '__main__':
    main()
