#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter09/verbose_http.py
# HTTP request handler for urllib2 that prints requests and responses.

import io, http.client, urllib.request, urllib.error, urllib.parse

class VerboseHTTPResponse(http.client.HTTPResponse):
    def _read_status(self):
        data = self.fp.read()
        print(data.decode('ascii'))
        self.fp = io.BytesIO(data)
        return http.client.HTTPResponse._read_status(self)

class VerboseHTTPConnection(http.client.HTTPConnection):
    response_class = VerboseHTTPResponse
    def send(self, data):
        nl = '' if data.endswith(b'\n') else '\n'
        print(data.decode('ascii'), end=nl)
        http.client.HTTPConnection.send(self, data)

class VerboseHTTPHandler(urllib.request.HTTPHandler):
    def http_open(self, req):
        return self.do_open(VerboseHTTPConnection, req)
