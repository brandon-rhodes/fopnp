#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - telnet_login.py
# Connect to localhost, watch for a login prompt, and try logging in

import telnetlib

t = telnetlib.Telnet('localhost')
# t.set_debuglevel(1)        # uncomment this for debugging messages

t.read_until(b'login:')
t.write(b'brandon\n')
t.read_until(b'assword:')     # let "P" be capitalized or not
t.write(b'mypass\n')
n, match, previous_text = t.expect([br'Login incorrect', br'\$'], 10)
if n == 0:
    print(b'Username and password failed - giving up')
else:
    t.write(b'exec uptime\n')
    print(t.read_all().decode('ascii'))  # read until connection closes
