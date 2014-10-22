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

One of the scripts is quite simple.  It tries to send a large UDP
datagram to learn the length of the largest packet that could actually
cross the network between its own host and the host named on the command
line.  Running it in the [Playground](../../playground#readme) should
report a maximum packet size of 1,500 bytes, the typical maximum length
on an Ethernet network:

```
$ python3 big_sender.py www.example.com
Alas, the datagram did not make it
Actual MTU: 1500
```

The other scripts are each a client-server pair, where the server should
be started in one terminal window and the client run in another.  The
`udp_local.py` server and client must be run on the same machine:

```
$ python3 udp_local.py server &>server.log &
```

```
$ python3 udp_local.py client
The OS assigned me the address ('0.0.0.0', 60442)
The server ('127.0.0.1', 1060) replied 'Your data was 38 bytes long'
```

```
$ cat server.log
Listening at ('127.0.0.1', 1060)
The client at ('127.0.0.1', 60442) says 'The time is 2014-10-22 14:52:25.936376'
```

The other two scripts can communicate between machines, and need
hostname arguments on the command line.  Read their source code, as well
as the book chapter, to learn how the scripts demonstrate successively
more powerful UDP abilities.
