#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/build_basic_email.py

from email.message import Message

text = """Hello,

This is a test message from Chapter 12.

 - Anonymous"""

def main():
    message = Message()
    message['To'] = 'recipient@example.com'
    message['From'] = 'Test Sender <sender@example.com>'
    message['Subject'] = 'Test Message, Chapter 12'
    message.set_payload(text)
    print(message.as_string())

if __name__ == '__main__':
    main()
