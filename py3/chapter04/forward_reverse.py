#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter04/forward_reverse.py
# Checking whether a host name works both forwards and backwards.

import argparse, socket, sys

def verify_hostname(hostname):
    try:
        infolist = socket.getaddrinfo(
            hostname, 0, 0, socket.SOCK_STREAM, 0,
            socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,
            )
    except socket.gaierror as e:
        print('Forward name service failure:', e)
        sys.exit(1)

    info = infolist[0]  # choose the first result tuple
    canonical_name = info[3]
    address = info[4]
    ip = address[0]

    if not canonical_name:
        print('WARNING!  The IP address', ip, 'has no reverse name')
        sys.exit(1)

    print(hostname, 'has IP address', ip)
    print(ip, 'has the canonical hostname', canonical_name)

    # Lowercase for case-insensitive comparison, and chop off hostnames.

    forward = hostname.lower().split('.')
    reverse = canonical_name.lower().split('.')

    if forward == reverse:
        print('The forward and reverse names agree completely')
        return True

    # Truncate the domain names, which now look like ['www', mit', 'edu'],
    # to the same length and compare.  Failing that, be willing to try a
    # compare with the first element (the hostname?) lopped off if both of
    # they are the same length.

    length = min(len(forward), len(reverse))
    if (forward[-length:] == reverse[-length:]
        or (len(forward) == len(reverse)
            and forward[-length+1:] == reverse[-length+1:]
            and len(forward[-2]) > 2)):  # avoid thinking '.co.uk' means a match!
        print('The forward and reverse names have a lot in common')
    else:
        print('WARNING!  The reverse name belongs to a different organization')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('hostname', help='')
    verify_hostname(parser.parse_args().hostname)
