[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 12<br>Building and Parsing E-Mail

This is a directory of program listings from Chapter 12 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

The scripts in this chapter work only in Python 3.4 and later, because
they take advantage of several innovations in the Standard Library
`email` module that have been recently introduced by R. David Murray.
If you are stuck on an older version of Python 3 then you will want to
visit the [`pre-python-3.4`](https://github.com/brandon-rhodes/fopnp/tree/m/py3/chapter12/pre-python-3.4)
subdirectory, where you can find the examples from the Second Edition of
the book updated for Python 3.  The original Python 2 examples are in
the [`py2/chapter12`](https://github.com/brandon-rhodes/fopnp/tree/m/py2/chapter12)
directory of this source code repository.

The simplest script builds an email message, which the book takes as a
basic example of what email looks like on the wire or when saved in a
raw form to disk by a mail spool or client.

```
$ python3 build_basic_email.py > mail.txt
```

```
$ cat mail.txt
To: recipient@example.com
From: Test Sender <sender@example.com>
Subject: Test Message, Chapter 12
Date: Tue, 25 Mar 2014 19:20:08 -0400
Message-ID: <20140325232008.15748.50494@guinness>
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0

Hello,
This is a basic message from Chapter 12.
 - Anonymous
```

An email client will typically hide most of these details from the user.
The `display_email.py` script is offered as an example of the kind of
information that the user might want to see when they view a message.

```
$ python3 display_email.py < mail.txt
From: Test Sender <sender@example.com>
To: recipient@example.com
Date: Tue, 25 Mar 2014 19:20:08 -0400
Subject: Test Message, Chapter 12

Hello,
This is a basic message from Chapter 12.
 - Anonymous

```

From these simple beginnings, the book progresses through more and more
complicated examples of MIME encoding until it has explained alternative
parts, related parts, and attachments.  All of these features can be
seen interacting in a single message by giving `build_mime_email.py`
exactly the right arguments:

```
$ python3 build_mime_email.py -i attachment.txt attachment.gz > mail.txt
```

```
$ cat mail.txt
To: Test Recipient <recipient@example.com>
From: Test Sender <sender@example.com>
Subject: Foundations of Python Network Programming
Date: Tue, 25 Mar 2014 19:20:08 -0400
Message-ID: <20140325232008.15748.50494@guinness>
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="===============0086939546=="

--===============0086939546==
Content-Type: multipart/alternative; boundary="===============0903170602=="

--===============0903170602==
Content-Type: multipart/related; boundary="===============1911784257=="

--===============1911784257==
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: 7bit

<p>Hello,</p>
<p>This is a <b>test message</b> from Chapter 12.</p>
<p>- <i>Anonymous</i></p><p>This is the smallest possible blue GIF:</p>
<img src="cid:20140325232008.15748.99346@guinness" height="80" width="80">

--===============1911784257==
Content-Type: image/gif
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="blue-dot.gif"
Content-ID: <20140325232008.15748.99346@guinness>
MIME-Version: 1.0

R0lGODlhAQABAJAAAAAA/wAAACwAAAAAAQABAAACAgQBADs=

--===============1911784257==--

--===============0903170602==
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0

Hello,
This is a MIME message from Chapter 12.
- Anonymous

--===============0903170602==--

--===============0086939546==
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="attachment.txt"
MIME-Version: 1.0

This is a test

--===============0086939546==
Content-Type: application/octet-stream
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="attachment.gz"
MIME-Version: 1.0

H4sIAP3o2D8AAwvJyCxWAKJEhZLU4hIuAIwtwPoPAAAA

--===============0086939546==--
```

The book then shows how this complexity is hidden from a typical email
user by invoking both the `display_email.py` script and also the more
low-level investigative `display_structure.py` script to look at the
email’s structure in fine details.  These scripts can also be used to
unravel complicated real-world emails from the reader’s own mailbox.

```
$ python3 display_email.py < mail.txt
From: Test Sender <sender@example.com>
To: Test Recipient <recipient@example.com>
Date: Tue, 25 Mar 2014 19:20:08 -0400
Subject: Foundations of Python Network Programming

Hello,
This is a MIME message from Chapter 12.
- Anonymous

* image/gif attachment named 'blue-dot.gif': bytes object of length 35
* text/plain attachment named 'attachment.txt': str object of length 15
* application/octet-stream attachment named 'attachment.gz': bytes object of length 33
```

```
$ python3 display_structure.py < mail.txt
 type=multipart/mixed
.0 type=multipart/alternative
.0.0 type=multipart/related
.0.0.0 type=text/html str len=215
.0.0.1 type=image/gif bytes len=35 attachment filename='blue-dot.gif'
.0.1 type=text/plain str len=59
.1 type=text/plain str len=15 attachment filename='attachment.txt'
.2 type=application/octet-stream bytes len=33 attachment filename='attachment.gz'
```

Finally, one last script lets the reader learn about how Unicode comes
into play when it appears in email headers and when it appears in the
body of an email.  Encoding is necessary in both cases, because neither
context traditionally allows anything except plain ASCII printable
characters.

```
$ python3 build_unicode_email.py > mail.txt
```

```
$ cat mail.txt
To: =?utf-8?b?QsO2w7B2YXJy?= <recipient@example.com>
From: Eardstapa <sender@example.com>
Subject: Four lines from The Wanderer
Date: Tue, 25 Mar 2014 19:20:08 -0400
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable
MIME-Version: 1.0

Hw=C3=A6r cwom mearg? Hw=C3=A6r cwom mago?
Hw=C3=A6r cwom ma=C3=BE=C3=BEumgyfa?
Hw=C3=A6r cwom symbla gesetu?
Hw=C3=A6r sindon seledreamas?
```

```
$ python3 display_email.py < mail.txt
From: Eardstapa <sender@example.com>
To: Böðvarr <recipient@example.com>
Date: Tue, 25 Mar 2014 19:20:08 -0400
Subject: Four lines from The Wanderer

Hwær cwom mearg? Hwær cwom mago?
Hwær cwom maþþumgyfa?
Hwær cwom symbla gesetu?
Hwær sindon seledreamas?

```

Consult the book chapter for all of the concepts and rules behind these
examples, as well as for further information about the options with
which you can invoke them.
