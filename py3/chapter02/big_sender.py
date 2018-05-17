#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/big_sender.py
# Send a big UDP datagram to learn the MTU of the network path.

import argparse, socket, sys

# Inlined constants, because Python 3.6 has dropped the IN module.

class IN:
    IP_MTU = 14
    IP_MTU_DISCOVER = 10
    IP_PMTUDISC_DO = 2

if sys.platform != 'linux':
    print('Unsupported: Can only perform MTU discovery on Linux',
          file=sys.stderr)
    sys.exit(1)

def send_big_datagram(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
    sock.connect((host, port))
    try:
        sock.send(b'#' * 999999)
    except socket.error:
        print('Alas, the datagram did not make it')
        max_mtu = sock.getsockopt(socket.IPPROTO_IP, IN.IP_MTU)
        print('Actual MTU: {}'.format(max_mtu))
    else:
        print('The big datagram was sent!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send UDP packet to get MTU')
    parser.add_argument('host', help='the host to which to target the packet')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    send_big_datagram(args.host, args.p)
