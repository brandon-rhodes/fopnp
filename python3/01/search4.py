#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search4.py

import socket
sock = socket.socket()
sock.connect(('maps.google.com', 80))
sock.sendall(
    b'GET /maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH'
    b'&output=json&oe=utf8&sensor=false HTTP/1.1\r\n'
    b'Host: maps.google.com:80\r\n'
    b'User-Agent: search4.py\r\n'
    b'Connection: close\r\n'
    b'\r\n')
rawreply = sock.recv(4096)
print(rawreply.decode('utf-8'))
