#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter06/test_tls.py
# Attempt a TLS connection and, if successful, report its properties

import argparse, socket, ssl, sys, textwrap
import ctypes
from pprint import pprint

def open_tls(address, server=False, ca_path=None, debug=False):

    say('Address we want to talk to', address)
    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_sock.connect(address)
    #context.load_cert_chain('../../playground/certs/www.pem')
    ssl_sock = context.wrap_socket(raw_sock)

    cert = ssl_sock.getpeercert()
    subject = cert.get('subject', [])
    names = [name for names in subject for (key, name) in names
             if key == 'commonName']
    if 'subjectAltName' in cert:
        names.extend(name for (key, name) in cert['subjectAltName']
                     if key == 'DNS')

    say('Name(s) on its server certificate', *names or ['no certificate'])
    if names:
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
    """Call match_hostname() and turn any exception into a string."""
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

def lookup(prefix, name):
    if not name.startswith(prefix):
        name = prefix + name
    try:
        return getattr(ssl, name)
    except AttributeError:
        matching_names = (s for s in dir(ssl) if s.startswith(prefix))
        message = 'Error: {!r} is not one of the available names:\n {}'.format(
            name, ' '.join(sorted(matching_names)))
        print(fill(message), file=sys.stderr)
        sys.exit(2)

def fill(text):
    return textwrap.fill(text, subsequent_indent='    ',
                         break_long_words=False, break_on_hyphens=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Protect a socket with TLS')
    parser.add_argument('host', help='hostname or IP address')
    parser.add_argument('port', type=int, help='TCP port number')
    parser.add_argument('-c', metavar='ca_cert', default=None,
                        help='specify CA certificate instead of default')
    parser.add_argument('-d', action='store_true', default=False,
                        help='debug mode: do not hide "ctypes" exceptions')
    parser.add_argument('-p', metavar='PROTOCOL', default='SSLv23',
                        help='protocol version (default: SSLv23)')
    parser.add_argument('-s', action='store_true', default=False,
                        help='run as the server instead of the client')
    parser.add_argument('-v', action='store_true', default=False,
                        help='verbose: print out certificate information')
    args = parser.parse_args()

    address = (args.host, args.port)
    protocol = lookup('PROTOCOL_', args.p)

    context = ssl.SSLContext(protocol)
    context.check_hostname = False
    if args.c is not None:
        context.load_verify_locations(args.c)

    print()
    cert = open_tls(address, args.s, args.c, args.d)
    print()
    if args.v:
        pprint(cert)
