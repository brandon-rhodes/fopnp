#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/big_sender.py
# Send a big UDP datagram to learn the MTU of the network path.

import IN, argparse, socket

def send_big_datagram(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
    s.connect((host, port))
    try:
        s.send(b'#' * 65000)
    except socket.error:
        print('Alas, the datagram did not make it')
        option = getattr(IN, 'IP_MTU', 14)  # constant from <linux/in.h>
        max_mtu = s.getsockopt(socket.IPPROTO_IP, option)
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
