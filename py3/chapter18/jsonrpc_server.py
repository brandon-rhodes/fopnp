#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_server.py
# JSON-RPC server needing "pip install jsonrpclib-pelix"

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def lengths(*args):
    """Measure the length of each input argument.

    Given N arguments, this function returns a list of N smaller
    lists of the form [len(arg), arg] that each state the length of
    an input argument and also echo back the argument itself.

    """
    results = []
    for arg in args:
        try:
            arglen = len(arg)
        except TypeError:
            arglen = None
        results.append((arglen, arg))
    return results

def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(lengths)
    print("Starting server")
    server.serve_forever()

if __name__ == '__main__':
    main()
