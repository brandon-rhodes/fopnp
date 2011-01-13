#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 5 - streamer.py
# Client that sends data then closes the socket, not expecting a reply.

import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = sys.argv.pop() if len(sys.argv) == 3 else '127.0.0.1'
PORT = 1060

if sys.argv[1:] == ['server']:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print('Listening at', s.getsockname())
    sc, sockname = s.accept()
    print('Accepted connection from', sockname)
    sc.shutdown(socket.SHUT_WR)
    message = b''
    while True:
        more = sc.recv(8192)  # arbitrary value of 8k
        if not more:  # socket has closed when recv() returns ''
            break
        message += more
    print('Done receiving the message; it says:')
    print(message.decode('ascii'))
    sc.close()
    s.close()

elif sys.argv[1:] == ['client']:
    s.connect((HOST, PORT))
    s.shutdown(socket.SHUT_RD)
    s.sendall(b'Beautiful is better than ugly.\n')
    s.sendall(b'Explicit is better than implicit.\n')
    s.sendall(b'Simple is better than complex.\n')
    s.close()

else:
    print('usage: streamer.py server|client [host]', file=sys.stderr)
