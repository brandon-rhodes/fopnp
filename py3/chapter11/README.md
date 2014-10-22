[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 11<br>The World Wide Web

This is a directory of program listings from Chapter 11 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

Chapter 11 is a sprawling exploration of the mere basics of what it
means to design a web application, that cannot usefully be summarized
here.  It begins with a simple application `app_insecure.py` written in
Flask that, upon closer inspection, winds up having four major security
flaws.  Each of these is in turn investigated, exploited, and then fixed
as the chapter proceeds.

Once the problems are fixed, the result is `app_improved.py`.  This site
raises an interesting question: how might a Python program download data
from an application with a properly functioning login page?  Trying to
simply download the home page results in a redirect demanding a login:

```
$ python3 app_improved.py &>server.log &
```

```
$ sleep 3 && curl -s http://127.0.0.1:5000/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="/login">/login</a>.  If not click the link.
```

The answer is that the Python program must write a custom web scraping
program that knows exactly how login to this particular site works.  The
`mscrape.py` is such a program, which can connect to the site either
using Request or by using Webdriver to program the operation of a real
web browser like Firefox.  It can then parse the results using either
BeautifulSoup or the more modern lxml library.  Either way, the result
should be a successful login followed by printing out the information
gleaned from the page’s HTML:

```
$ python3 mscrape.py http://127.0.0.1:5000/
         125  Registration for PyCon
         200  Payment for writing that code
    --------  ------------------------------
         325  Total payments made
```

Turning back to the server log, we see how our attempt to GET the site
root resulted only in a 302 redirect.  The `mscrape.py` logic, by
contrast, was able to POST exactly the right credentials to the login
page to get past it to a successful GET of the site root:

```
$ cat server.log
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
127.0.0.1 - - [25/Mar/2014 19:20:08] "GET / HTTP/1.1" 302 -
127.0.0.1 - - [25/Mar/2014 19:20:08] "POST /login HTTP/1.1" 302 -
127.0.0.1 - - [25/Mar/2014 19:20:08] "GET / HTTP/1.1" 200 -
```

The chapter makes several key comparisons between micro-frameworks and
full-stack web frameworks by comparing the Flask based `app_improved.py`
with the same application rewritten from the ground up in Django.  Its
code lives in the `djbank` directory here, and it can be started with
its `manage.py` script:

    $ python3 manage.py runserver

Finally, the chapter turns to the question of scraping large web sites,
where instead of a single page being targeted there might be dozens or
hundreds of pages, whose URLs might not even be known until they turn up
in the text of other pages.  Both `rscrape1.py` and `rscrape2.py`
demonstrate the basic techniques, and are designed for use against a
small static site that the chapter presents in the `tinysite` directory.
You can serve this site up using Python’s built-in web server:

```
$ (cd tinysite && python3 -m http.server) &>server.log &
```

The first scraper merely performs GETs of the URLs it can plainly see on
each page, and can only visit a small portion of the site:

```
$ python3 rscrape1.py http://127.0.0.1:8000/
GET http://127.0.0.1:8000/
GET http://127.0.0.1:8000/page2.html
GET http://127.0.0.1:8000/page1.html
```

The second scraper is more bold: by adding more dangerous operations
like POST, and by being willing to drive a real web browser whose
JavaScript can load dynamic content, it can visit all of the pages on
the site.

```
$ python3 rscrape2.py http://127.0.0.1:8000/
GET http://127.0.0.1:8000/
submit_form http://127.0.0.1:8000/
GET http://127.0.0.1:8000/page2.html
GET http://127.0.0.1:8000/page4.html
GET http://127.0.0.1:8000/page5.html
GET http://127.0.0.1:8000/page1.html
GET http://127.0.0.1:8000/page3.html
GET http://127.0.0.1:8000/page6.html
```
