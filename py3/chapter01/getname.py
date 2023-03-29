#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/getname.py

import socket

if __name__ == '__main__':
    # 'maps.google.com'의 IP 주소를 얻고자 한다. 방법은 다음과 같다.
    # hostname is the name of the server we want to connect to // host, hostname, domain name
    hostname = 'maps.google.com'
    # gethostbyname() returns the IP address of the server
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))
