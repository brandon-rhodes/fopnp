#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/pre-python-3.4/mime_structure.py

import email, fileinput

def print_message(message, level = 0):
    prefix = "|  " * level
    prefix2 = prefix + "|"
    print(prefix + "+ Message Headers:")
    for header, value in message.items():
        print(prefix2, header + ":", value)
    if message.is_multipart():
        for item in message.get_payload():
            print_message(item, level + 1)

message = email.message_from_string(''.join(fileinput.input()))
print_message(message)
