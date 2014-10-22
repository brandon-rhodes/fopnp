[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 3<br>TCP

This is a directory of program listings from Chapter 3 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

These scripts were written for Python 3, but can also run successfully
under Python 2.  Simply use [3to2](https://pypi.python.org/pypi/3to2) to
convert them to the older syntax.

There are only two scripts featured in this chapter, both of which
illustrate the TCP stream oriented protocol through a small client and
server.  Neither script needs its client and server to be run on
different hosts to illustrate the features of TCP, though their command
line arguments do permit it.  The `tcp_sixteen.py` script simply sends
and receives sixteen bytes of data in each direction:

```
$ python3 tcp_sixteen.py server '' &>server.log &
```

```
$ python3 tcp_sixteen.py client localhost
Client has been assigned socket name ('127.0.0.1', 34183)
The server said b'Farewell, client'
```

```
$ cat server.log
Listening at ('0.0.0.0', 1060)
Waiting to accept a new connection
We have accepted a connection from ('127.0.0.1', 34183)
  Socket name: ('127.0.0.1', 1060)
  Socket peer: ('127.0.0.1', 34183)
  Incoming sixteen-octet message: b'Hi there, server'
  Reply sent, socket closed
Waiting to accept a new connection
```

The `tcp_deadlock.py` script, by contrast, illustrates how incautious
use of a stream protocol can fill the operating system network buffers
and lead to deadlock.
