#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/mime_decode.py

import argparse, email.message, email.policy

def walk(message, level=0):
    yield (level, message)
    if message.get_content_maintype() == 'multipart':
        for part in message.iter_parts():
            yield from walk(part, level + 1)

def save_parts(message):
    counter = 0
    for level, message in walk(message):
        indent = '  ' * level
        if message.get_content_maintype() == 'multipart':
            print(counter, indent, message.get_content_type())
        else:
            counter += 1
            filename = 'part{}.out'.format(counter)
            print(counter, indent, message.get_content_type(),
                  message.get('content-disposition', '-'), '=>', filename)
            content = message.get_content()
            mode = 'w' if isinstance(content, str) else 'wb'
            with open(filename, mode) as f:
                f.write(content)

def main():
    parser = argparse.ArgumentParser(description='Save message in part*.txt')
    parser.add_argument('filename', help='Input email message filename')
    with open(parser.parse_args().filename) as f:
        save_parts(email.message_from_file(f, policy=email.policy.default))

if __name__ == '__main__':
    main()
