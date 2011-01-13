#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - getname.py

import socket
hostname = 'maps.google.com'
addr = socket.gethostbyname(hostname)
print 'The address of', hostname, 'is', addr
