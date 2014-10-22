[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 6<br>TLS/SSL

This is a directory of program listings from Chapter 6 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

The scripts in this chapter are a rare example of code from this book
that simply **will not work** under Python 2 — and, in fact, that will
not work under Python 3.3 or earlier — because the `ssl` module of those
Python versions lack the `create_default_context()` call that these
Python 3.4 scripts use to configure TLS settings that are both safe and
secure.  See [PEP-466](http://legacy.python.org/dev/peps/pep-0466/) for
the ongoing effort to bring these features to the next release of
Python 2.7, because of how crucial they are for network security.

I strongly recommend that you read the chapter, and not simply read
these example scripts, if you want to learn what TLS is designed to
accomplish and what is at stake in all of the decisions that the
protocol offers to its users.

The scripts in this chapter can operate between hosts, either in the
[Playground](../../playground#readme) or on real machines.  The scripts
should also work just fine on one machine if you connect to `localhost`,
in which case you can use the simple `ca.crt` and `localhost.pem` that
are sitting in this directory.

The `safe_tls.py` script illustrates how to set up a TLS connection in
Python 3.4 and later using the secure defaults it provides.

```
$ python3 safe_tls.py -s localhost.pem '' 1060 &>server.log &
```

```
$ python3 safe_tls.py -a ca.crt localhost 1060
Connected to host 'localhost' and port 1060
b'Simple is better than complex.'
```

```
$ cat server.log
Listening at interface '' and port 1060
Connection from host '127.0.0.1' and port 41252
```

If you want more information about how TLS settings relate to the
protocol version and ciphers that the client and server actually
negotiate, you can run the more detailed `test_tls.py` script that does
its best to inspect and report on as many details of the protocol as the
`ssl` module is willing to expose.

```
$ python3 test_tls.py -s localhost.pem localhost 1060 &>server.log &
```

```
$ python3 test_tls.py -a ca.crt localhost 1060

Address we want to talk to.......... ('localhost', 1060)
Peer certificate.................... provided
Name(s) on peer certificate......... localhost
Whether name(s) match the hostname.. Yes
Certificates loaded of type crl..... 0
Certificates loaded of type x509.... 1
Certificates loaded of type x509_ca. 0
Protocol version negotiated......... TLSv1.2
Cipher chosen for this connection... ECDHE-RSA-AES256-GCM-SHA384
Cipher defined in TLS version....... TLSv1/SSLv3
Cipher key has this many bits....... 256
Compression algorithm in use........ none

```

```
$ cat server.log

Interface where we are listening.... ('localhost', 1060)
Client has connected from address... ('127.0.0.1', 41254)
Peer certificate.................... none
Protocol version negotiated......... TLSv1.2
Cipher chosen for this connection... ECDHE-RSA-AES256-GCM-SHA384
Cipher defined in TLS version....... TLSv1/SSLv3
Cipher key has this many bits....... 256
Compression algorithm in use........ none

```

You can consult the chapter as well as the command-line options that
`test_tls.py` will print with the `-h` option if you want to learn about
all of the TLS settings — include client certificates — to which it
gives you access.

Finally, as a small bonus for those looking at these scripts online, I
include the `features.py` script that I used when writing the chapter.
It looks at your `ssl` module and reports on what options are offered in
your version of Python.

```
$ python3 features.py

------------------------------- protocol -------------------------------
PROTOCOL_SSLv2                       0                                 0
PROTOCOL_SSLv3                       1                                 1
PROTOCOL_SSLv23                      2                                10
PROTOCOL_TLSv1                       3                                11
PROTOCOL_TLSv1_1                     4                               100
PROTOCOL_TLSv1_2                     5                               101

----------------------------- verify_mode ------------------------------
CERT_NONE                            0                                 0
CERT_OPTIONAL                        1                                 1
CERT_REQUIRED                        2                                10

----------------------------- verify_flags -----------------------------
VERIFY_DEFAULT                       0                                 0
VERIFY_CRL_CHECK_LEAF                4                               100
VERIFY_CRL_CHECK_CHAIN              12                              1100
VERIFY_X509_STRICT                  32                            100000

------------------------------- options --------------------------------
OP_NO_COMPRESSION               131072                100000000000000000
OP_SINGLE_ECDH_USE              524288              10000000000000000000
OP_SINGLE_DH_USE               1048576             100000000000000000000
OP_CIPHER_SERVER_PREFERENCE    4194304           10000000000000000000000
OP_NO_SSLv2                   16777216         1000000000000000000000000
OP_NO_SSLv3                   33554432        10000000000000000000000000
OP_NO_TLSv1                   67108864       100000000000000000000000000
OP_NO_TLSv1_2                134217728      1000000000000000000000000000
OP_NO_TLSv1_1                268435456     10000000000000000000000000000
OP_ALL                      2147484671  10000000000000000000001111111111

------------------------- feature availability -------------------------
HAS_ECDH                             1                                 1
HAS_NPN                              1                                 1
HAS_SNI                              1                                 1

```
