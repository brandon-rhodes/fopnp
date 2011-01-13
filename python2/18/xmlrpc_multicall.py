#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 18 - xmlrpc_multicall.py
# XML-RPC client performing a multicall

import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://127.0.0.1:7001')
multicall = xmlrpclib.MultiCall(proxy)
multicall.addtogether('a', 'b', 'c')
multicall.quadratic(2, -4, 0)
multicall.remote_repr([1, 2.0, 'three'])
for answer in multicall():
    print answer
