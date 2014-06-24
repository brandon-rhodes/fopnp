#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter06/tls_example.py
# Building an encrypted TLS connection

import argparse, os, socket, ssl, sys
import ctypes
from ctypes import POINTER, Structure, c_char_p, c_ulong, c_void_p, cast
from pprint import pprint

def client(hostname, port, debug=False):
    #ctypes.cdll.LoadLibrary(ssl._ssl.__file__)
    # print(ssl.__file__)
    # print(ssl._ssl.__file__)
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
    #print(context.get_ca_certs()[1])  # TODO: full list?

    # Does the certificate that the server proffered *really* match the
    # hostname to which we are trying to connect?  We need to check.

    #print(sock.compression())
    pprint(sock.getpeercert())

    try:
        ssl.match_hostname(sock.getpeercert(), hostname)
    except ssl.CertificateError as ce:
        print('Certificate error:', str(ce))
        sys.exit(1)

    print('Cipher:', sock.cipher())

    try:
        print('PROTOCOL VERSION:', repr(SSL_get_version(sock)))
    except Exception:
        if debug:
            raise

    # From here on, our `sock` works like a normal socket.  We can,
    # for example, make an impromptu HTTP call.

    sock.sendall(b'GET / HTTP/1.0\r\n\r\n')
    result = sock.makefile().read()  # quick way to read until EOF
    sock.close()
    print('The document https://%s/ is %d bytes long' % (hostname, len(result)))

class PySSLSocket(Structure):
    """The first few fields of a PySSLSocket (see Python's Modules/_ssl.c)."""
    _fields_ = [('ob_refcnt', c_ulong), ('ob_type', c_void_p),
                ('Socket', c_void_p), ('ssl', c_void_p)]

def SSL_get_version(ssl_sock):
    """Reach behind the scenes for a socket's TLS protocol version."""
    lib = ctypes.CDLL(ssl._ssl.__file__)
    lib.SSL_get_version.restype = ctypes.c_char_p
    address = id(ssl_sock._sslobj)
    struct = cast(address, POINTER(PySSLSocket)).contents
    version_bytestring = lib.SSL_get_version(struct.ssl)
    return version_bytestring.decode('ascii')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Protect a socket with TLS')
    parser.add_argument('host', help='remote host to which to connect')
    parser.add_argument('-p', metavar='PORT', type=int, default=443,
                        help='TCP port (default 443)')
    parser.add_argument('-d', action='store_true', default=False,
                        help='debug mode: do not hide "ctypes" exceptions')
    args = parser.parse_args()
    client(args.host, args.p, args.d)
