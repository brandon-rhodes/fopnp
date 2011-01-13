#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 18 - rpyc_server.py
# RPyC server

import rpyc

class MyService(rpyc.Service):
    def exposed_line_counter(self, fileobj, function):
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MyService, port = 18861)
t.start()
