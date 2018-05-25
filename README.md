
# Foundations of Python Network Programming

Welcome!

This GitHub repository offers all of the example Python code from the
Third Edition of *Foundations of Python Network Programming* as revised by
[Brandon Rhodes](http://rhodesmill.org/brandon/) for Python 3:

<a href="http://www.amazon.com/gp/product/1430258543/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1430258543&linkCode=as2&tag=letsdisthemat-20&linkId=QLZVTAMAR4QVX32Q"><img border="0" src="http://ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=1430258543&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=letsdisthemat-20" ></a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=letsdisthemat-20&l=as2&o=1&a=1430258543" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

<a href="http://www.amazon.com/gp/product/1430258543/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1430258543&linkCode=as2&tag=letsdisthemat-20&linkId=MQI66M23YQHP4SY2">From Amazon.com (affiliate link)</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=letsdisthemat-20&l=as2&o=1&a=1430258543" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
<br>
<a href="http://www.apress.com/9781430258544">From Apress (the publisher)</a>

Each chapter’s source code lives in its own directory:

*   [Chapter 1: Introduction to Client-Server Networking](py3/chapter01#readme)
*   [Chapter 2: UDP](py3/chapter02#readme)
*   [Chapter 3: TCP](py3/chapter03#readme)
*   [Chapter 4: Socket Names and DNS](py3/chapter04#readme)
*   [Chapter 5: Network Data and Network Errors](py3/chapter05#readme)
*   [Chapter 6: TLS/SSL](py3/chapter06#readme)
*   [Chapter 7: Server Architecture](py3/chapter07#readme)
*   [Chapter 8: Caches and Message Queues](py3/chapter08#readme)
*   [Chapter 9: HTTP Clients](py3/chapter09#readme)
*   [Chapter 10: HTTP Servers](py3/chapter10#readme)
*   [Chapter 11: The World Wide Web](py3/chapter11#readme)
*   [Chapter 12: Building and Parsing E-Mail](py3/chapter12#readme)
*   [Chapter 13: SMTP](py3/chapter13#readme)
*   [Chapter 14: POP](py3/chapter14#readme)
*   [Chapter 15: IMAP](py3/chapter15#readme)
*   [Chapter 16: Telnet and SSH](py3/chapter16#readme)
*   [Chapter 17: FTP](py3/chapter17#readme)
*   [Chapter 18: RPC](py3/chapter18#readme)

## Most of this works under Python 2

If you are still using Python 2, you will still benefit from studying
these examples as they are more carefully designed than the scripts in
the previous edition and also use more modern third-party libraries.

The `README.md` inside each chapter directory — which GitHub will
display automatically when you click a chapter title in the Table of
Contents above — has a paragraph near the top stating whether the
scripts work with Python 2 or not.  Typically each script needs only a
quick run through the [3to2](https://pypi.python.org/pypi/3to2) tool in
order to operate flawlessly under the old version of the language.

The exceptions are:

 *  The TLS/SSL examples in Chapter 6 are specific to Python 3.4 and
    later because only with that version of the language did the `ssl`
    module gain safe enough defaults to be recommended for use with
    secure services.  (An effort to backport these features to
    Python 2.7, however, does seem to be underway.)

 *  Two of the scripts in Chapter 8 run into a snag if translated to
    Python 2 because of modules that have switched whether they want to
    operate on bytes or on Unicode strings.

 *  The `email` scripts in Chapter 12 use a new and more convenient API
    that was added to the language in Python 3.4.

The other changes between Python 2 and 3 will be handled automatically
by 3to2: `print()` is now a function, plain `b'byte strings'` now take a
leading `b`, and many Standard Library modules were renamed during the
transition.

## The Network Playground

Many novice network programmers do not have interesting networks to
explore — many homes have only a laptop plus a broadband modem to which
the homeowner does not have access.

To remedy this situation, I have developed an entire [Network
Playground](playground) consisting of more than a half dozen hosts
providing services from SSH and Telnet to a web server and FTP.  The
“hosts” are built using Docker, and I hope soon to package the whole
thing up as a virtual machine that users can download.

The result will be that the user can get a prompt from which they can
connect out to the `example.com` server farm and talk to all kinds of
network services.  And just as in a real network, they will find that
these machines are several hops away — hops that can be inspected by
normal networking tools like `traceroute`:

```
$ ssh h1

# traceroute www.example.com
traceroute to www.example.com (10.130.1.4), 30 hops max, 60 byte packets
 1  192.168.1.1 (192.168.1.1)  0.513 ms  0.208 ms  0.265 ms
 2  isp (10.25.1.1)  0.544 ms  0.220 ms  0.115 ms
 3  backbone (10.1.1.1)  0.364 ms  0.227 ms  0.252 ms
 4  example.com (10.130.1.1)  0.617 ms  0.355 ms  0.407 ms
 5  www.example.com (10.130.1.4)  1.301 ms  0.415 ms  0.522 ms
```

You can find the instructions here: [The Network Playground](playground).
