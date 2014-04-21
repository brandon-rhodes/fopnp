#!/usr/bin/env python2
#
# HTTP and HTTPS server based partly upon:
# http://www.piware.de/2011/01/creating-an-https-server-in-python/

import BaseHTTPServer, SimpleHTTPServer
import argparse
import os
import ssl
import threading

this_dir = os.path.dirname(os.path.abspath(__file__))

def main(pempath):
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    h80 = BaseHTTPServer.HTTPServer(('0.0.0.0', 80), handler)
    t = threading.Thread(target=h80.serve_forever)
    t.daemon = True
    t.start()

    h443 = BaseHTTPServer.HTTPServer(('0.0.0.0', 443), handler)
    h443.socket = ssl.wrap_socket(h443.socket,
                                  certfile=pempath, server_side=True)
    h443.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Combined HTTP/HTTPS server')
    parser.add_argument('pempath', help='path to PEM certificate+key file')
    args = parser.parse_args()
    cwd = os.getcwd()
    os.chdir(this_dir + '/../../py3')  # serve the Python 3 book examples
    main(os.path.join(cwd, args.pempath))
