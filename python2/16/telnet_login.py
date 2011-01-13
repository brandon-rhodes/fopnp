#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - telnet_login.py
# Connect to localhost, watch for a login prompt, and try logging in

import telnetlib

t = telnetlib.Telnet('localhost')
# t.set_debuglevel(1)        # uncomment this for debugging messages

t.read_until('login:')
t.write('brandon\n')
t.read_until('assword:')     # let "P" be capitalized or not
t.write('mypass\n')
n, match, previous_text = t.expect([r'Login incorrect', r'\$'], 10)
if n == 0:
    print "Username and password failed - giving up"
else:
    t.write('exec uptime\n')
    print t.read_all()       # keep reading until the connection closes
