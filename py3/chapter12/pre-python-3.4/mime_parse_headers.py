#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/pre-python-3.4/mime_parse_headers.py

import email, fileinput
from email.header import decode_header

message = email.message_from_string(''.join(fileinput.input()))
for header, raw in list(message.items()):
    value = ''.join(
        data if isinstance(data, str) else data.decode(charset or 'ascii')
        for data, charset in decode_header(raw)
        )
    print('{0}: {1}'.format(header, value))
