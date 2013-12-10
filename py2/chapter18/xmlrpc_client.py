#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Foundations of Python Network Programming - Chapter 18 - xmlrpc_client.py
# XML-RPC client

import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://127.0.0.1:7001')
print proxy.addtogether('x', 'ÿ', 'z')
print proxy.addtogether(20, 30, 4, 1)
print proxy.quadratic(2, -4, 0)
print proxy.quadratic(1, 2, 1)
print proxy.remote_repr((1, 2.0, 'three'))
print proxy.remote_repr([1, 2.0, 'three'])
print proxy.remote_repr({'name': 'Arthur', 'data': {'age': 42, 'sex': 'M'}})
print proxy.quadratic(1, 0, 1)
