# HTTP and HTTPS server based partly upon:
# http://www.piware.de/2011/01/creating-an-https-server-in-python/

from http.server import HTTPServer, SimpleHTTPRequestHandler
from ssl import wrap_socket
import argparse
import os
import threading

def main(pempath):
    h80 = HTTPServer(('0.0.0.0', 80), SimpleHTTPRequestHandler)
    threading.Thread(target=h80.serve_forever).start()

    h443 = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)
    h443.socket = wrap_socket(h443.socket, certfile=pempath, server_side=True)
    h443.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Combined HTTP/HTTPS server')
    parser.add_argument('pempath', help='path to PEM certificate+key file')
    parser.add_argument('directory', help='directory to serve as a web site')
    args = parser.parse_args()
    pempath = os.path.join(os.getcwd(), args.pempath)
    directory = os.path.join(os.getcwd(), args.directory)
    os.chdir(directory)
    main(pempath)
