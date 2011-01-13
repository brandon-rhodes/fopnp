#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 11 - wsgi_app.py
# A simple web application built directly against the low-level WSGI spec.

import cgi, base64
from wsgiref.simple_server import make_server

def page(content, *args):
    yield b'<html><head><title>wsgi_app.py</title></head><body>'
    yield (content % args).encode('utf-8')
    yield b'</body>'

def simple_app(environ, start_response):
    html_headers = [('Content-Type', 'text/html; charset=UTF-8')]
    gohome = '<br><a href="/">Return to the home page</a>'
    q = cgi.parse_qs(environ['QUERY_STRING'])

    if environ['PATH_INFO'] == '/':

        if environ['REQUEST_METHOD'] != 'GET' or environ['QUERY_STRING']:
            start_response('400 Bad Request', [('Content-Type', 'text/plain')])
            return [b'Error: the front page is not a form']

        start_response('200 OK', html_headers)
        return page('Welcome! Enter a string: <form action="encode">'
                    '<input name="mystring"><input type="submit"></form>')

    elif environ['PATH_INFO'] == '/encode':

        if environ['REQUEST_METHOD'] != 'GET':
            start_response('400 Bad Request', [('Content-Type', 'text/plain')])
            return [b'Error: this form does not support POST parameters']

        if 'mystring' not in q or not q['mystring'][0]:
            start_response('400 Bad Request', [('Content-Type', 'text/plain')])
            return [b'Error: this form requires a "mystring" parameter']

        my = q['mystring'][0]
        my64 = base64.b64encode(my.encode('utf-8')).decode('ascii')
        start_response('200 OK', html_headers)
        return page('<tt>%s</tt> base64 encoded is: <tt>%s</tt>' + gohome,
                    cgi.escape(repr(my)), cgi.escape(my64))

    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'That URL is not valid']

print('Listening on localhost:8000')
make_server('localhost', 8000, simple_app).serve_forever()
