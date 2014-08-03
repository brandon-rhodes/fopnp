#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/zen_example.py
# Constants and routines for supporting a certain network conversation.

import argparse, socket

proverbs = {b'Beautiful is better than?': b'Ugly.',
            b'Explicit is better than?': b'Implicit.',
            b'Simple is better than?': b'Complex.'}

def get_answer(proverb):
    return proverbs.get(proverb, b'Error: unknown proverb.')

def parse_command_line(description):
    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address

def create_server_socket(address):
    """Build and return a listening server socket."""
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print('Listening at {}:{}'.format(*address))
    return listener

def handle_client_conversation(sock):
    """Converse with a client over `sock` until they are done talking."""
    try:
        while True:
            handle_client_request(sock)
    except EOFError:
        print('Client has finished and closed socket')
    except Exception as e:
        print('Error: {}'.format(e))
        sock.close()

def handle_client_request(sock):
    """Receive a single client request on `sock` and send the answer."""
    proverb = recv_until(sock, b'?')
    answer = get_answer(proverb)
    sock.sendall(answer)

def recv_until(sock, suffix):
    """Receive bytes over socket `sock` until we receive the `suffix`."""
    message = sock.recv(4096)
    if not message:
        raise EOFError('socket closed')
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError('received truncated data {!r}'.format(data))
        message += data
    return message
