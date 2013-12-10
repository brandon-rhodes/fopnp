#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter09/get_rfc2616.py
# Example use of the verbose HTTP request handler.

import urllib, urllib.request, urllib.error, urllib.parse
from verbose_http import VerboseHTTPHandler
opener = urllib.request.build_opener(VerboseHTTPHandler)
opener.open('http://www.ietf.org/rfc/rfc2616.txt')
