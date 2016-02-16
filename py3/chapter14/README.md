[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 14<br>POP

This is a directory of program listings from Chapter 14 of the book:

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

You should probably never use the scripts in this chapter, as the POP
protocol is unreliable, poorly designed and implemented on servers, and
should be abandoned in favor of IMAP.  See the chapter for details.

The scripts in this chapter are best exercised inside the network
[Playground](../../playground#readme) where `mail.example.com` is
already set up and configured for POP.  Once the playground is running,
ask for a prompt on the `h1` host and visit this chapter’s directory:

    $ ./play.sh h1

    # cd py3/chapter14

All of the scripts in this chapter are careful to use the `POP3_SSL`
class and therefore guarantee the use of TLS to protect the user’s
password and prevent other people in the same coffee shop from seeing
the user’s email.  The `popconn.py` script simply connects and reports
the number of messages waiting:

```
$ python3 popconn.py mail.example.com brandon
Password: abc123
You have 6 messages totaling 3441 bytes
```

The `apopconn.py` script does exactly the same thing, but using a
variant of the standard authentication methods.  The `mailbox.py` script
asks the server for a list of the messages that are waiting, and prints
a brief summary about each one.

```
$ python3 mailbox.py mail.example.com brandon
Password: abc123
Message 1 has 354 bytes
Message 2 has 442 bytes
Message 3 has 1175 bytes
Message 4 has 491 bytes
Message 5 has 490 bytes
Message 6 has 489 bytes
```

Finally, the `download_and_delete.py` script lets the user interactively
view each message and decide whether to ask the server to delete it.
