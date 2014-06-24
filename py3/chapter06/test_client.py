#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter06/test_client.py
# Attempt a TLS connection and, if successful, report its properties

import argparse, socket, ssl, textwrap
import ctypes
from pprint import pprint

def open_ssl_connection(hostname, port, debug=False):
    say('Server we want to talk to', hostname)
    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_sock.connect((hostname, port))
    context = ssl.create_default_context()
    context.check_hostname = False
    ssl_sock = context.wrap_socket(raw_sock)

    cert = ssl_sock.getpeercert()
    names = [name for names in cert['subject'] for (kind, name) in names
             if kind == 'commonName']
    if 'subjectAltName' in cert:
        names.extend(name for s, name in cert['subjectAltName'] if s == 'DNS')

    say('Name(s) on its server certificate', *names)
    say('Whether name(s) match the hostname', test(cert, hostname))
    for category, count in sorted(context.cert_store_stats().items()):
        say('Certificates loaded of type {}'.format(category), count)

    try:
        protocol_version = SSL_get_version(ssl_sock)
    except Exception:
        if debug:
            raise
    else:
        say('Protocol version negotiated', protocol_version)

    cipher, version, bits = ssl_sock.cipher()
    compression = ssl_sock.compression()

    say('Cipher chosen for this connection', cipher)
    say('Cipher defined in TLS version', version)
    say('Cipher key has this many bits', bits)
    say('Compression algorithm in use', compression or 'none')

    return cert

def say(title, *words):
    text = title.ljust(36, '.') + ' ' + ' '.join(str(w) for w in words)
    print(textwrap.fill(text, subsequent_indent=' ' * 8,
                        break_long_words=False, break_on_hyphens=False))

def test(cert, hostname):
    """Convert the result of match_hostname() (an exception) to a string."""
    try:
        ssl.match_hostname(cert, hostname)
    except ssl.CertificateError as e:
        return str(e)
    else:
        return 'Yes'

class PySSLSocket(ctypes.Structure):
    """The first few fields of a PySSLSocket (see Python's Modules/_ssl.c)."""

    _fields_ = [('ob_refcnt', ctypes.c_ulong), ('ob_type', ctypes.c_void_p),
                ('Socket', ctypes.c_void_p), ('ssl', ctypes.c_void_p)]

def SSL_get_version(ssl_sock):
    """Reach behind the scenes for a socket's TLS protocol version."""

    lib = ctypes.CDLL(ssl._ssl.__file__)
    lib.SSL_get_version.restype = ctypes.c_char_p
    address = id(ssl_sock._sslobj)
    struct = ctypes.cast(address, ctypes.POINTER(PySSLSocket)).contents
    version_bytestring = lib.SSL_get_version(struct.ssl)
    return version_bytestring.decode('ascii')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Protect a socket with TLS')
    parser.add_argument('host', help='remote host to which to connect')
    parser.add_argument('-p', metavar='PORT', type=int, default=443,
                        help='TCP port (default 443)')
    parser.add_argument('-c', action='store_true', default=False,
                        help='pretty-print certificate information')
    parser.add_argument('-d', action='store_true', default=False,
                        help='debug mode: do not hide "ctypes" exceptions')
    args = parser.parse_args()
    print()
    cert = open_ssl_connection(args.host, args.p, args.d)
    print()
    if args.c:
        pprint(cert)
