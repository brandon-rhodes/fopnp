#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 18 - jsonrpc_client.py
# JSON-RPC client

from lovely.jsonrpc import proxy
proxy = proxy.ServerProxy('http://localhost:7002')
print proxy.lengths((1,2,3), 27, {'Sirius': -1.46, 'Rigel': 0.12})
