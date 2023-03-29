#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter03/tcp_deadlock.py
# TCP client and server that leave too much data waiting

import argparse, socket, sys

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    # 앞서 bind가 서버소켓에서 필수로 사용된다고 말했듯이, 이 listen도 서버소켓에서밖에 쓰일 일이 없습니다.
    # listen()안에 인자로 숫자 1이 입력되어 있는데, 이는 해당 소켓이 총 몇개의 동시접속까지를 허용할 것이냐는 이야기입니다.
    # 1을 입력하면 단 한 개의 접속만을 허용할 것이고, 인자를 입력하지 않으면 파이썬이 자의적으로 판단해서 임의의 숫자로 listen한다고 합니다.
    sock.listen(1)
    print('Listening at', sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        print('Processing up to 1024 bytes at a time from', sockname)
        n = 0
        while True:
            data = sc.recv(1024)
            # 더 이상 보낼 데이터가 없다면 루프에서 나온다.
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sc.sendall(output)  # send it back uppercase
            n += len(data)
            print('\r  %d bytes processed so far' % (n,), end=' ')
            sys.stdout.flush()
        print()
        # 데이터 전송이 끝났으면 끝낸다.
        sc.close()
        print('  Socket closed')

def client(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = (bytecount + 15) // 16 * 16  # round up to a multiple of 16
    message = b'capitalize this!'  # 16-byte message to repeat over and over

    print('Sending', bytecount, 'bytes of data, in chunks of 16 bytes')
    sock.connect((host, port))

    sent = 0
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print('\r  %d bytes sent' % (sent,), end=' ')
        sys.stdout.flush()

    print()
    sock.shutdown(socket.SHUT_WR)

    print('Receiving all the data the server sends back')

    received = 0
    while True:
        data = sock.recv(42)
        if not received:
            print('  The first data received says', repr(data))
        if not data:
            break
        received += len(data)
        print('\r  %d bytes received' % (received,), end=' ')

    print()
    sock.close()

if __name__ == '__main__':
    roles = ('client', 'server')
    parser = argparse.ArgumentParser(description='Get deadlocked over TCP')
    parser.add_argument('role', choices=roles, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('bytecount', type=int, nargs='?', default=16,
                        help='number of bytes for client to send (default 16)')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    if args.role == 'client':
        client(args.host, args.p, args.bytecount)
    else:
        server(args.host, args.p)
