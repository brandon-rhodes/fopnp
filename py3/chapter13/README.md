[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 13<br>SMTP

This is a directory of program listings from Chapter 13 of the book:

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

The scripts in this chapter are best exercised inside the network
[Playground](../../playground#readme) where `mail.example.com` is
already set up and configured to receive incoming email.  Once the
playground is running, ask for a prompt on the `h1` host and visit the
`chapter13` directory:

    $ ssh h1

    # cd /fopnp/py3/chapter13

At the `h1` machine’s prompt you can then experiment with sending
messages across the network.  The `simple.py` script and the slightly
more advanced `ehlo.py` do their work silently, while `debug.py` asks
the Standard Library to show the communication that is going on at the
socket level.

```
$ python3 simple.py mail.example.com sender@example.com brandon@example.com
Message sent to 1 recipient
```

```
$ python3 ehlo.py mail.example.com sender@example.com brandon@example.com
Maximum message size is 10240000
Message sent to 1 recipient
```

```
$ python3 debug.py mail.example.com sender@example.com brandon@example.com
send: 'ehlo [172.17.0.10]\r\n'
reply: b'250-mail.example.com\r\n'
reply: b'250-PIPELINING\r\n'
reply: b'250-SIZE 10240000\r\n'
reply: b'250-VRFY\r\n'
reply: b'250-ETRN\r\n'
reply: b'250-STARTTLS\r\n'
reply: b'250-ENHANCEDSTATUSCODES\r\n'
reply: b'250-8BITMIME\r\n'
reply: b'250 DSN\r\n'
reply: retcode (250); Msg: b'mail.example.com\nPIPELINING\nSIZE 10240000\nVRFY\nETRN\nSTARTTLS\nENHANCEDSTATUSCODES\n8BITMIME\nDSN'
send: 'mail FROM:<sender@example.com> size=210\r\n'
reply: b'250 2.1.0 Ok\r\n'
reply: retcode (250); Msg: b'2.1.0 Ok'
send: 'rcpt TO:<brandon@example.com>\r\n'
reply: b'250 2.1.5 Ok\r\n'
reply: retcode (250); Msg: b'2.1.5 Ok'
send: 'data\r\n'
reply: b'354 End data with <CR><LF>.<CR><LF>\r\n'
reply: retcode (354); Msg: b'End data with <CR><LF>.<CR><LF>'
data: (354, b'End data with <CR><LF>.<CR><LF>')
send: b'To: brandon@example.com\r\nFrom: sender@example.com\r\nSubject: Test Message from simple.py\r\n\r\nHello,\r\n\r\nThis is a test message sent to you from the debug.py program\r\nin Foundations of Python Network Programming.\r\n.\r\n'
reply: b'250 2.0.0 Ok: queued as 98034261\r\n'
reply: retcode (250); Msg: b'2.0.0 Ok: queued as 98034261'
data: (250, b'2.0.0 Ok: queued as 98034261')
Message sent to 1 recipient
send: 'quit\r\n'
reply: b'221 2.0.0 Bye\r\n'
reply: retcode (221); Msg: b'2.0.0 Bye'
```

After connecting to the `mail` machine with the username `brandon` and
the password `abc123` you can use the venerable `mail` command to see
that three new test messages are in your mailbox, thanks to the three
Python scripts that you just ran:

    # ssh brandon@mail.example.com
    brandon@mail.example.com's password: abc123

    You have new mail.

    $ mail
    "/var/mail/brandon": 6 messages 6 new
    >N   1 Administrator      Tue Mar 25 17:14   9/345   Welcome to example.com!
     N   2 Administrator      Mon Apr 21 12:08  11/431   Introduction to e-mail
     N   3 Test Sender        Mon Apr 21 13:41  40/1135  Foundations of Python Net
     N   4 sender@example.com Wed Oct 22 20:34  14/477   Test Message from simple.
     N   5 sender@example.com Wed Oct 22 20:34  14/476   Test Message from simple.
     N   6 sender@example.com Wed Oct 22 20:35  14/475   Test Message from simple.
    ? q
    Held 6 messages in /var/mail/brandon

The `login.py` and `tls.py` scripts are for the more advanced cases
where an SMTP server requires authentication or TLS encryption —
situations for which the Playground SMTP server is not yet configured.

<!-- TODO -->
