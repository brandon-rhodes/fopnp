#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/pre-python-3.4/trad_parse.py
# Traditional Message Parsing

import email

banner = '-' * 48
popular_headers = {'From', 'To', 'Subject', 'Date'}
with open('message.txt') as f:
    msg = email.message_from_file(f)
headers = sorted(msg.keys())

print(banner)
for header in headers:
    if header not in popular_headers:
        print(header + ':', msg[header])
print(banner)
for header in headers:
    if header in popular_headers:
        print(header + ':', msg[header])

print(banner)
if msg.is_multipart():
    print("This program cannot handle MIME multipart messages.")
else:
    print(msg.get_payload())
