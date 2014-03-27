#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/build_basic_email.py

import email.message

text = """Hello,
This is a basic message from Chapter 12.
 - Anonymous"""

def main():
    message = email.message.Message()
    message['To'] = 'recipient@example.com'
    message['From'] = 'Test Sender <sender@example.com>'
    message['Subject'] = 'Test Message, Chapter 12'
    message.set_payload(text)
    print(message.as_string())

if __name__ == '__main__':
    main()
