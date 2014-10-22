[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 4<br>Socket Names and DNS

This is a directory of program listings from Chapter 4 of the book:

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
to the older syntax.  The `www_ping.py` script will then need a small
tweak: change the string literal `u'www'` to simply `'www'` in its call
to `getaddrinfo()` or you will get a socket error.

The chapter gives a tour of DNS and how it provides worldwide name
resolution.  The three scripts involved are conceptually quite simple.
The first asks the operating system to do its usual name resolution, and
presents the normal pattern by which Python programs should resolve a
name before opening a socket.

```
$ python3 www_ping.py www.google.com
Success: host www.google.com is listening on port 80
```

The second two dig into the DNS protocol itself using the third-party
`dnspython3` package:

```
$ python3 dns_basic.py www.google.com
<DNS www.google.com. IN A RRset>
<DNS www.google.com. IN AAAA RRset>
```

```
$ python3 dns_mx.py google.com
This domain has 5 MX records
Priority 10
     aspmx.l.google.com has A address 64.233.171.27
Priority 20
     alt1.aspmx.l.google.com has A address 64.233.186.27
Priority 30
     alt2.aspmx.l.google.com has A address 74.125.24.27
Priority 40
     alt3.aspmx.l.google.com has A address 74.125.206.27
Priority 50
     alt4.aspmx.l.google.com has A address 173.194.65.27
```

The chapter outlines how to properly use the logic inside of `dns_mx.py`
to power your own SMTP email delivery system so that it obeys the
relevant standards for sending messages to big sites like Google.
