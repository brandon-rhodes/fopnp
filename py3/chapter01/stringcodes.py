#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/stringcodes.py

if __name__ == '__main__':
    # Translating from the outside world of bytes to Unicode characters.
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_characters = input_bytes.decode('utf-16')
    print(repr(input_characters))

    # Translating characters back into bytes before sending them.
    output_characters = 'We copy you down, Eagle.\n'
    output_bytes = output_characters.encode('utf-8')
    with open('eagle.txt', 'wb') as f:
        f.write(output_bytes)
