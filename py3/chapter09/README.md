[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 9<br>HTTP Clients

This is a directory of program listings from Chapter 9 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

Chapter 9 is a detailed tour of HTTP and its features, illuminated by a
series of live examples at the Python prompt.  The examples are
collected here in the `examples.doctest` which you can run on your own
system if you first install `gunicorn` and `httpbin` and then run them
using the command listed at the top of `config.py`:

    $ gunicorn -c config.py httpbin:app

The doctest file can then be exercised, if you have `requests`
installed, with:

    $ python3 -m doctest examples.doctest

All three of these dependencies will be installed automatically if you
install everything in [`requirements.txt`](https://github.com/brandon-rhodes/fopnp/blob/m/py3/requirements.txt).

If you are interested in trying out these examples under Python 2, you
will find that the code that uses `requests` will usually work without
any change, while all of the code that needs `urllib` or `http` from the
Standard Library will need to be reworked to use the old names for those
libraries instead.  Running [3to2](https://pypi.python.org/pypi/3to2) on
any of the example code, once you have pasted it into a plain `.py`
file, should perform the renaming needed to get the code ready to run
under Python 2.
