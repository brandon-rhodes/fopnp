#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 12 - mime_parse_headers.py

import sys, email
from email.header import decode_header

msg = email.message_from_file(sys.stdin)
for header, raw in list(msg.items()):
    parts = decode_header(raw)
    value = ''
    for data, charset in parts:
        if isinstance(data, str):
            value += data
        else:
            value += data.decode(charset or 'ascii')
    print('{0}: {1}'.format(header, value))
