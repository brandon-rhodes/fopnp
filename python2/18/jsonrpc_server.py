#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 18 - jsonrpc_server.py
# JSON-RPC server

from wsgiref.simple_server import make_server
import lovely.jsonrpc.dispatcher, lovely.jsonrpc.wsgi

def lengths(*args):
    results = []
    for arg in args:
        try:
            arglen = len(arg)
        except TypeError:
            arglen = None
        results.append((arglen, arg))
    return results

dispatcher = lovely.jsonrpc.dispatcher.JSONRPCDispatcher()
dispatcher.register_method(lengths)
app = lovely.jsonrpc.wsgi.WSGIJSONRPCApplication({'': dispatcher})
server = make_server('localhost', 7002, app)
print "Starting server"
while True:
    server.handle_request()
