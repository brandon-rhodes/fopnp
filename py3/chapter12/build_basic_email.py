#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/build_basic_email.py

from email.message import EmailMessage

text = """Hello,

This is a test message from Chapter 12.

 - Anonymous"""

def main():
    msg = EmailMessage()
    msg['To'] = 'recipient@example.com'
    msg['From'] = 'Test Sender <sender@example.com>'
    msg['Subject'] = 'Test Message, Chapter 12'
    msg.set_content(text)
    print(msg.as_string())

if __name__ == '__main__':
    main()
