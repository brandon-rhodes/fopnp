#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter03/tcp_deadlock.py
# TCP client and server that leave too much data waiting

import argparse, socket, sys

def server(host, port, bytecount):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    print('Listening at', s.getsockname())
    while True:
        sc, sockname = s.accept()
        print('Processing up to 1024 bytes at a time from', sockname)
        n = 0
        while True:
            data = sc.recv(bytecount)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sc.sendall(output)  # send it back uppercase
            n += len(data)
            print('\r  %d bytes processed so far' % (n,), end=' ')
            sys.stdout.flush()
        print()
        sc.close()
        print('  Socket closed')

def client(host, port, bytecount):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = (bytecount + 15) // 16 * 16  # round up to a multiple of 16
    message = b'capitalize this!'  # 16-byte message to repeat over and over

    print('Sending', bytecount, 'bytes of data, in chunks of 16 bytes')
    s.connect((host, port))

    sent = 0
    while sent < bytecount:
        s.sendall(message)
        sent += len(message)
        print('\r  %d bytes sent' % (sent,), end=' ')
        sys.stdout.flush()

    print()
    s.shutdown(socket.SHUT_WR)

    print('Receiving all the data the server sends back')

    received = 0
    while True:
        data = s.recv(42)
        if not received:
            print('  The first data received says', repr(data))
        if not data:
            break
        received += len(data)
        print('\r  %d bytes received' % (received,), end=' ')

    print()
    s.close()

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Get deadlocked over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('bytecount', type=int, nargs='?', default=16,
                        help='number of bytes for client to send, or for'
                        ' server to recv() at once (default 16)')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p, args.bytecount)
