[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 5<br>Network Data and Network Errors

This is a directory of program listings from Chapter 5 of the book:

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

This chapter tackles the issue of encoding and framing network data,
discussing many small examples that are collected here in the source
code repository as the `examples.rst` file.  In addition, there are two
scripts that then bring together the bigger ideas in the chapter.  The
first is a small client and server that perform no framing, but simply
close the socket to let their peer know when they are done:

```
$ python3 streamer.py '' &>server.log &
```

```
$ python3 streamer.py -c localhost
```

```
$ cat server.log
Run this script in another window with "-c" to connect
Listening at ('0.0.0.0', 1060)
Accepted connection from ('127.0.0.1', 40613)
Received 96 bytes
Received zero bytes - end of file
Message:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.

```

The second client prepends explicit binary framing into each message it
sends, so that the server can extract them each from the socket stream
without ambiguity.

```
$ python3 blocks.py '' &>server.log &
```

```
$ python3 blocks.py -c localhost
```

```
$ cat server.log
Run this script in another window with "-c" to connect
Listening at ('0.0.0.0', 1060)
Accepted connection from ('127.0.0.1', 40615)
Block says: b'Beautiful is better than ugly.'
Block says: b'Explicit is better than implicit.'
Block says: b'Simple is better than complex.'
```

In retrospect, these clients are a little bit quiet for my taste.  They
should probably have at least printed something to their standard out,
so that it is clear that they are trying to accomplish something.  As it
stands, the user has to look at the terminal window where the server is
running to be convinced that the client really sent anything over the
network.

See the book chapter for the lessons that can be drawn from each of
these two designs, and about the other possible approaches — beyond this
simple pair of mechanisms — that network protocols can adopt.
