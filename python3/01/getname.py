#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 1 - getname.py

import socket

if __name__ == '__main__':
    hostname = 'maps.google.com'
    addr = socket.gethostbyname(hostname)
    print('The IP address of', hostname, 'is', addr)
