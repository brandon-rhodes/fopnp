#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter16/telnet_codes.py
# How your code might look if you intercept Telnet options yourself

import argparse, getpass
from telnetlib import Telnet, IAC, DO, DONT, WILL, WONT, SB, SE, TTYPE

def process_option(tsocket, command, option):
    if command == DO and option == TTYPE:
        tsocket.sendall(IAC + WILL + TTYPE)
        print('Sending terminal type "mypython"')
        tsocket.sendall(IAC + SB + TTYPE + b'\0' + b'mypython' + IAC + SE)
    elif command in (DO, DONT):
        print('Will not', ord(option))
        tsocket.sendall(IAC + WONT + option)
    elif command in (WILL, WONT):
        print('Do not', ord(option))
        tsocket.sendall(IAC + DONT + option)

def main(hostname, username, password):
    t = Telnet(hostname)
    # t.set_debuglevel(1)        # uncomment to get debug messages
    t.set_option_negotiation_callback(process_option)
    t.read_until(b'login:', 10)
    t.write(username.encode('utf-8') + b'\r')
    t.read_until(b'assword:', 10)    # first letter might be 'p' or 'P'
    t.write(password.encode('utf-8') + b'\r')
    n, match, previous_text = t.expect([br'Login incorrect', br'\$'], 10)
    if n == 0:
        print("Username and password failed - giving up")
    else:
        t.write(b'exec echo My terminal type is $TERM\n')
        print(t.read_all().decode('ascii'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Use Telnet to log in')
    parser.add_argument('hostname', help='Remote host to telnet to')
    parser.add_argument('username', help='Remote username')
    args = parser.parse_args()
    password = getpass.getpass()
    main(args.hostname, args.username, password)
