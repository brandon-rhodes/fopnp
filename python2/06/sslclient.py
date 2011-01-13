#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 6 - sslclient.py
# Using SSL to protect a socket in Python 2.6 or later

import os, socket, ssl, sys
from backports.ssl_match_hostname import match_hostname, CertificateError

try:
    script_name, hostname = sys.argv
except ValueError:
    print >>sys.stderr, 'usage: sslclient.py <hostname>'
    sys.exit(2)

# First we connect, as usual, with a socket.

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, 443))

# Next, we turn the socket over to the SSL library!

ca_certs_path = os.path.join(os.path.dirname(script_name), 'certfiles.crt')
sslsock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv3,
                          cert_reqs=ssl.CERT_REQUIRED, ca_certs=ca_certs_path)

# Does the certificate that the server proffered *really* match the
# hostname to which we are trying to connect?  We need to check.

try:
    match_hostname(sslsock.getpeercert(), hostname)
except CertificateError, ce:
    print 'Certificate error:', str(ce)
    sys.exit(1)

# From here on, our `sslsock` works like a normal socket.  We can, for
# example, make an impromptu HTTP call.

sslsock.sendall('GET / HTTP/1.0\r\n\r\n')
result = sslsock.makefile().read()  # quick way to read until EOF
sslsock.close()
print 'The document https://%s/ is %d bytes long' % (hostname, len(result))
