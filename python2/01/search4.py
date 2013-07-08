#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search4.py

import socket
import sys

sock = socket.socket()
sock.connect(('maps.google.com', 80))
sock.sendall(
    'GET /maps/api/geocode/json?sensor=false'
    '&address=207+N.+Defiance+St%2C+Archbold%2C+OH HTTP/1.0\r\n'
    'Host: maps.google.com:80\r\n'
    'User-Agent: search4.py\r\n'
    'Connection: close\r\n'
    '\r\n')

while True:
    rawdata = sock.recv(4096)
    if rawdata == '':
        break
    sys.stdout.write(rawdata)
