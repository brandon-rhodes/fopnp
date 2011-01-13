#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 - verbose_handler.py
# Example use of the verbose HTTP request handler.

import urllib, urllib.request, urllib.error, urllib.parse
from verbose_http import VerboseHTTPHandler
opener = urllib.request.build_opener(VerboseHTTPHandler)
opener.open('http://www.ietf.org/rfc/rfc2616.txt')
