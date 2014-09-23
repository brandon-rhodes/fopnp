#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter10/timeapp_webob.py
# A WSGI callable built using webob.

import time, webob

def app(environ, start_response):
    request = webob.Request(environ)
    if environ['REQUEST_METHOD'] != 'GET':
        response = webob.Response('501 Not Implemented', status=501)
    elif request.domain != '127.0.0.1' or request.path != '/':
        response = webob.Response('404 Not Found', status=404)
    else:
        response = webob.Response(time.ctime())
    return response(environ, start_response)
