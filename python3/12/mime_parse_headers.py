#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 12 - mime_parse_headers.py

import email, fileinput
from email.header import decode_header

message = email.message_from_string(''.join(fileinput.input()))
for header, raw in list(message.items()):
    value = ''.join(
        data if isinstance(data, str) else data.decode(charset or 'ascii')
        for data, charset in decode_header(raw)
        )
    print('{0}: {1}'.format(header, value))
