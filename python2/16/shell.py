#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - shell.py
# A simple shell, so you can try running commands in the absence of
# any special characters (except for whitespace, used for splitting).

import subprocess

while True:
    args = raw_input('] ').split()
    if not args:
        pass
    elif args == ['exit']:
        break
    elif args[0] == 'show':
        print "Arguments:", args[1:]
    else:
        subprocess.call(args)
