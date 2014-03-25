#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/parse_basic.py

import argparse, email.policy

def main(filename):
    with open(parser.parse_args().filename) as f:
        msg = email.message_from_file(f, policy=email.policy.default)

    popular_headers = {'From', 'To', 'Subject', 'Date'}
    print(' Display Headers '.center(40, '-'))
    for header in sorted(set(msg) & popular_headers):
        print(header + ':', msg[header])
    print(' Other Headers '.center(40, '-'))
    for header in sorted(set(msg) - popular_headers):
        print(header + ':', msg[header])
    print(' Body '.center(40, '-'))
    try:
        body = msg.get_body(preferencelist=('plain', 'html'))
    except KeyError:
        print('<This message lacks a printable text or HTML body>')
    else:
        print(body.get_content())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse an email message')
    parser.add_argument('filename', help='Input email message filename')
    main(parser.parse_args().filename)
