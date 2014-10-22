[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 2<br>UDP

This is a directory of program listings from Chapter 2 of the book:

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

```
$ python big_sender.py www.example.com
Alas, the datagram did not make it
Actual MTU: 1500
```

```
$ python udp_broadcast.py server localhost & echo hi
hi
```

```
$ python udp_broadcast.py client localhost
```
Traceback (most recent call last):
  File "udp_broadcast.py", line 35, in <module>
    function(args.host, args.p)
  File "udp_broadcast.py", line 12, in server
    sock.bind((interface, port))
  File "/usr/lib/python2.7/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 98] Address already in use
