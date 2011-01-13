#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - telnet_codes.py
# How your code might look if you intercept Telnet options yourself

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

t = Telnet('localhost')
# t.set_debuglevel(1)        # uncomment this for debugging messages

t.set_option_negotiation_callback(process_option)
t.read_until(b'login:', 5)
t.write(b'brandon\n')
t.read_until(b'assword:', 5)  # so P can be capitalized or not
t.write(b'mypass\n')
n, match, previous_text = t.expect([br'Login incorrect', br'\$'], 10)
if n == 0:
    print("Username and password failed - giving up")
else:
    t.write(b'exec echo My terminal type is $TERM\n')
    print(t.read_all().decode('ascii'))
