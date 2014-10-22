[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 8<br>Caches and Message Queues

This is a directory of program listings from Chapter 8 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

The scripts here in Chapter 8 can run into a few snags if you try
converting them to Python 2, because of differences in how both the
`hashlib` Standard Library module and the third-party `memcache` package
treat bytes and strings differently under Python 2 versus Python 3.  If
you are still using Python 2, try consulting the three scripts from
Chapter 8 in the [previous edition of the book.](https://github.com/brandon-rhodes/fopnp/tree/m/py2/chapter08)

The three scripts in this chapter power its discussion of caches and
message queues — network services which are fundamental to how modern
services scale out to very large numbers of clients.

The `squares.py` script requires you to install `memcached` on your
system, along with a Python library for communicating with it — which
should already be available if you have installed everything in this
repository’s [`requirements.txt`](https://github.com/brandon-rhodes/fopnp/blob/m/py3/requirements.txt).

```
$ python3 squares.py
Ten successive runs:
 3.01s 2.14s 1.61s 1.16s 0.90s 0.70s 0.57s 0.50s 0.43s 0.37s
```

The `hashing.py` script needs only the Standard Library.

```
$ python3 hashing.py
alpha
   server0 35285 0.36
   server1 22674 0.23
   server2 29097 0.29
   server3 12115 0.12

hash
   server0 24748 0.25
   server1 24743 0.25
   server2 24943 0.25
   server3 24737 0.25

md5
   server0 24777 0.25
   server1 24820 0.25
   server2 24717 0.25
   server3 24857 0.25

```

The `queuepi.py` script instead requires `pyzmq` in order to run, but
does not require any central message queue to be running.  It uses a
rather abstruse set of cooperating workers.

```
$ python3 queuepi.py
Y 4.0
Y 4.0
Y 4.0
Y 4.0
Y 4.0
N 3.3333333333333335
N 2.857142857142857
N 2.5
N 2.2222222222222223
N 2.0
.
.
.
Y 3.1297185998627315
Y 3.130017152658662
N 3.128943758573388
Y 3.1292423723003084
Y 3.1295407813570937
Y 3.129838985954094
Y 3.1301369863013697
N 3.12906538856556
N 3.1279945242984257
Y 3.128292849811837
```
