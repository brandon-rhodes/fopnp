[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 18<br>RPC

This is a directory of program listings from Chapter 18 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

These scripts were written for Python 3, but most of them will run under
Python 2.  Use [3to2](https://pypi.python.org/pypi/3to2) to convert them
to the older syntax.  The exception is that `xmlrpc_client.py` runs into
trouble because it attempts to send Unicode strings in its RPC call, but
the Standard Library `xmlrpclib` does not know how to encode them.

The chapter explores three kinds of RPC: XML-RPC, JSON-RPC, and a
Python-specific system called RPyC.  The XML-RPC protocol is supported
by the Standard Library, while the other two require third-party
packages from the Python Package Index.

In each case, the chapter provides both a small sample server and then a
client that puts the server through its paces.  As all of the examples
are hard-coded to use `localhost`, they can all be safely run right on
your machine.

## XML-RPC

```
$ python3 xmlrpc_server.py &>server.log &
```

```
$ python3 xmlrpc_client.py
xÿz
55
[0.0, 8.0]
[-1.0]
[1, 2.0, 'three']
[1, 2.0, 'three']
{'data': {'age': 42, 'sex': 'M'}, 'name': 'Arthur'}
Traceback (most recent call last):
  ...
xmlrpc.client.Fault: <Fault 1: "<class 'ValueError'>:math domain error">
```

```
$ python3 xmlrpc_introspect.py
Here are the functions supported by this server:
addtogether(...)
   Add together everything in the list `things`.
quadratic(...)
   Determine `x` values satisfying: `a` * x*x + `b` * x + c == 0
remote_repr(...)
   Return the `repr()` rendering of the supplied `arg`.
```

```
$ python3 xmlrpc_multicall.py
abc
[0.0, 8.0]
[1, 2.0, 'three']
```

```
$ cat server.log
Server ready
127.0.0.1 - - [25/Mar/2014 19:20:08] "POST /RPC2 HTTP/1.1" 200 -
127.0.0.1 - - [25/Mar/2014 19:20:08] "POST /RPC2 HTTP/1.1" 200 -
...
127.0.0.1 - - [25/Mar/2014 19:20:08] "POST /RPC2 HTTP/1.1" 200 -
127.0.0.1 - - [25/Mar/2014 19:20:08] "POST /RPC2 HTTP/1.1" 200 -
```

## JSON-RPC

```
$ python3 jsonrpc_server.py &>server.log &
```

```
$ python3 jsonrpc_client.py
[[3, [1, 2, 3]], [None, 27], [2, {'Rigel': 0.12, 'Sirius': -1.46}]]
```

```
$ cat server.log
Starting server
127.0.0.1 - - [25/Mar/2014 19:20:08] "POST / HTTP/1.1" 200 -
```

## RPyC

```
$ python3 rpyc_server.py &>server.log &
```

```
$ python3 rpyc_client.py
Noisy: 'Simple\n'
Noisy: 'is\n'
Noisy: 'better\n'
Noisy: 'than\n'
Noisy: 'complex.\n'
The number of lines in the file was 5
```

```
$ cat server.log
Client has invoked exposed_line_counter()
```

Consult the chapter to learn about how RPyC is quite different from the
other mechanisms.  While the other two only support simple function
invocation, RPyC is in fact a general two-way object publishing
protocol.
