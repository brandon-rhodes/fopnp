#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter06/tls_example.py
# Building an encrypted TLS connection

import argparse, os, socket, ssl, sys
import ctypes
from ctypes import POINTER, Structure, c_char_p, c_ulong, c_void_p, cast
from pprint import pprint

class PySSLSocket(Structure):
    "Python object that wraps an SSL socket (see Python's Modules/_ssl.c)."
    _fields_ = [
        ('ob_refcnt', c_ulong),
        ('ob_type', c_void_p),
        ('Socket', c_void_p),
        ('ssl', c_void_p),
        # plus several more
        ]

def client(hostname, port):
    #ctypes.cdll.LoadLibrary(ssl._ssl.__file__)
    lib = ctypes.CDLL(ssl._ssl.__file__)
    # print(ssl.__file__)
    # print(ssl._ssl.__file__)
    print(lib.SSL_get_version)
    # print('VERSION:', lib.SSL_version())

    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_sock.connect((hostname, port))
    ca_certs_path = os.path.join(os.path.dirname(__file__), 'certfiles.crt')
    sock = ssl.wrap_socket(raw_sock,
                           ssl_version=ssl.PROTOCOL_SSLv23,
                           #ssl_version=ssl.PROTOCOL_TLSv1_2,
                           cert_reqs=ssl.CERT_REQUIRED,
                           ca_certs=ca_certs_path)

    print(ssl.create_default_context().check_hostname)
    print(ssl.create_default_context().protocol)

    context = sock.context
    print(context.check_hostname)
    print(context.cert_store_stats())
    print(context.get_ca_certs()[1])  # TODO: full list?

    # Does the certificate that the server proffered *really* match the
    # hostname to which we are trying to connect?  We need to check.

    #print(sock.compression())
    print(dir(sock))
    print(sock.proto)
    print('V:', sock.ssl_version)
    pprint(sock.getpeercert())

    try:
        ssl.match_hostname(sock.getpeercert(), hostname)
    except ssl.CertificateError as ce:
        print('Certificate error:', str(ce))
        sys.exit(1)

    print('Cipher:', sock.cipher())

    print(dir(sock))
    sock_struct = cast(id(sock._sslobj), POINTER(PySSLSocket)).contents
    # b = sock
    # c = sock
    print('refcnt:', sock_struct.ob_refcnt)
    print('type:', sock_struct.ob_type)
    print('Socket:', sock_struct.Socket)
    print('ssl:', sock_struct.ssl)

    lib.SSL_get_version.restype = c_char_p

    version = lib.SSL_version(sock_struct.ssl)
    print('VERSION A:', version, bin(version)[2:])
    print('VERSION B:', lib.SSL_get_version(sock_struct.ssl).decode('ascii'))

    for symbol in dir(ssl):
        if symbol.startswith('PROTOCOL_'):
            value = getattr(ssl, symbol)
            print(symbol, value, bin(value)[2:])

    for symbol in dir(ssl):
        if symbol.endswith('_VERSION'):
            value = getattr(ssl, symbol)
            print(symbol, value) #, bin(value)[2:])

    # From here on, our `sock` works like a normal socket.  We can,
    # for example, make an impromptu HTTP call.

    sock.sendall(b'GET / HTTP/1.0\r\n\r\n')
    result = sock.makefile().read()  # quick way to read until EOF
    sock.close()
    print('The document https://%s/ is %d bytes long' % (hostname, len(result)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Protect a socket with TLS')
    parser.add_argument('host', help='remote host to which to connect')
    parser.add_argument('-p', metavar='PORT', type=int, default=443,
                        help='TCP port (default 443)')
    args = parser.parse_args()
    client(args.host, args.p)
