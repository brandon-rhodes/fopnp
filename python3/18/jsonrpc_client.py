#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 18 - jsonrpc_client.py
# JSON-RPC client needing "pip install jsonrpclib-pelix"

from jsonrpclib import Server
proxy = Server('http://localhost:7002')
print(proxy.lengths((1,2,3), 27, {'Sirius': -1.46, 'Rigel': 0.12}))
