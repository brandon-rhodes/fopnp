#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 9 - verbose_handler.py
# HTTP request handler for urllib2 that prints requests and responses.

import io, http.client, urllib.request, urllib.error, urllib.parse

class VerboseHTTPResponse(http.client.HTTPResponse):
    def _read_status(self):
        s = self.fp.read()
        print('-' * 20, 'Response', '-' * 20)
        print(s.split(b'\r\n\r\n')[0].decode('ascii'))
        self.fp = io.BytesIO(s)
        return http.client.HTTPResponse._read_status(self)

class VerboseHTTPConnection(http.client.HTTPConnection):
    response_class = VerboseHTTPResponse
    def send(self, s):
        print('-' * 50)
        print(s.strip().decode('ascii'))
        http.client.HTTPConnection.send(self, s)

class VerboseHTTPHandler(urllib.request.HTTPHandler):
    def http_open(self, req):
        return self.do_open(VerboseHTTPConnection, req)
