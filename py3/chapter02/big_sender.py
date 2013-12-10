#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/big_sender.py
# Send a big UDP datagram to our server.

import IN, socket, sys

def send_big_datagram(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
    s.connect((host, port))
    try:
        s.send(b'#' * 65000)
    except socket.error:
        option = getattr(IN, 'IP_MTU', 14)  # constant from <linux/in.h>
        max_mtu = s.getsockopt(socket.IPPROTO_IP, option)
        print('Alas, the datagram did not make it')
        print('Actual MTU: {}'.format(max_mtu))
    else:
        print('The big datagram was sent!')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: big_sender.py <host>', file=sys.stderr)
        sys.exit(2)
    host = sys.argv[1]
    port = 1060
    send_big_datagram(host, port)
