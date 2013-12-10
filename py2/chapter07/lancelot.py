#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - lancelot.py
# Constants and routines for supporting a certain network conversation.

import socket, sys

PORT = 1060
qa = (('What is your name?', 'My name is Sir Lancelot of Camelot.'),
      ('What is your quest?', 'To seek the Holy Grail.'),
      ('What is your favorite color?', 'Blue.'))
qadict = dict(qa)

def recv_until(sock, suffix):
    message = ''
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise EOFError('socket closed before we saw %r' % suffix)
        message += data
    return message

def setup():
    if len(sys.argv) != 2:
        print >>sys.stderr, 'usage: %s interface' % sys.argv[0]
        exit(2)
    interface = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, PORT))
    sock.listen(128)
    print 'Ready and listening at %r port %d' % (interface, PORT)
    return sock
