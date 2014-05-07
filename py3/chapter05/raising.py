import socket
address = ('bad.hostname', 1234)
sock = socket.socket()

class DestinationError(Exception):
    def __str__(self):
        return '%s: %s' % (self.args[0], self.__cause__.strerror)

try:
    host = sock.connect(address)
except socket.error as e:
    raise DestinationError('Error connecting to destination') from e
