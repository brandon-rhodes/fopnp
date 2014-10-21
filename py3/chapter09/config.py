# A Gunicorn configuration file that I used during the writing of
# Foundations of Python Network Programming, Third Edition, to print out
# various HTTP requests and responses.
#   - Brandon Rhodes

"""Gunicorn configuration that prints HTTP to the screen.

To use this Gunicorn configuration, which prints HTTP requests and
responses to the screen, with the httpbin application, run the
following command in this directory after pip installing both
"gunicorn" and "httpbin" under Python 3:

    gunicorn -c config.py httpbin:app

"""
workers = 1
worker_class = 'sync'

def printout(data):
    """Print and then return the given data."""
    print(data.decode('utf-8'))
    return data

class Noisy:
    def __init__(self, sock): self.sock = sock
    def recv(self, count): return printout(self.sock.recv(count))
    def send(self, data): return self.sock.send(printout(data))
    def sendall(self, data): return self.sock.sendall(printout(data))
    def __getattr__(self, name): return getattr(self.sock, name)

def post_fork(server, worker):
    def accept():
        client, addr = _accept()
        return Noisy(client), addr
    sock = worker.sockets[0]
    _accept = sock.accept
    sock.accept = accept
