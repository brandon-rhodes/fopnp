#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter06/tls_example.py
# Building an encrypted TLS connection

import argparse
import os, socket, ssl, sys

def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))
    ca_certs_path = os.path.join(os.path.dirname(__file__), 'certfiles.crt')
    sslsock = ssl.wrap_socket(sock,
                              ssl_version=ssl.PROTOCOL_SSLv3,
                              cert_reqs=ssl.CERT_REQUIRED,
                              ca_certs=ca_certs_path)

    # Does the certificate that the server proffered *really* match the
    # hostname to which we are trying to connect?  We need to check.

    try:
        ssl.match_hostname(sslsock.getpeercert(), hostname)
    except ssl.CertificateError as ce:
        print('Certificate error:', str(ce))
        sys.exit(1)

    print('Cipher:', sslsock.cipher())

    # From here on, our `sslsock` works like a normal socket.  We can,
    # for example, make an impromptu HTTP call.

    sslsock.sendall(b'GET / HTTP/1.0\r\n\r\n')
    result = sslsock.makefile().read()  # quick way to read until EOF
    sslsock.close()
    print('The document https://%s/ is %d bytes long' % (hostname, len(result)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Protect a socket with TLS')
    parser.add_argument('host', help='remote host to which to connect')
    parser.add_argument('-p', metavar='PORT', type=int, default=443,
                        help='TCP port (default 443)')
    args = parser.parse_args()
    client(args.host, args.p)
