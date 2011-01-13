#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 18 - xmlrpc_introspect.py
# XML-RPC client

import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://127.0.0.1:7001')

print 'Here are the functions supported by this server:'
for method_name in proxy.system.listMethods():

    if method_name.startswith('system.'):
        continue

    signatures = proxy.system.methodSignature(method_name)
    if isinstance(signatures, list) and signatures:
        for signature in signatures:
            print '%s(%s)' % (method_name, signature)
    else:
        print '%s(...)' % (method_name,)

    method_help = proxy.system.methodHelp(method_name)
    if method_help:
        print '  ', method_help
