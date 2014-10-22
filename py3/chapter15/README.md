[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 15<br>IMAP

This is a directory of program listings from Chapter 15 of the book:

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
already set up and configured for POP.  Once the playground is running,
ask for a prompt on the `h1` host and visit this chapter’s directory:

    $ ./play.sh h1

    # cd py3/chapter14

The scripts will all need the password of the `brandon` user, which is
`abc123` and in the following examples will be piped in with the `echo`
command.  One lone script, `open_maplib.py`, uses the Standard Library
`imaplib` module:

```
$ echo abc123 | python3 open_imaplib.py mail.example.com brandon
Capabilities: ('IMAP4REV1', 'LITERAL+', 'SASL-IR', 'LOGIN-REFERRALS',
'ID', 'ENABLE', 'IDLE', 'AUTH=PLAIN')
Listing mailboxes 
Status: 'OK'
Data:
b'(\\HasNoChildren) "/" INBOX'
```

All of the other scripts, for technical issues explained in the chapter,
use the third party `imapclient` module by Menno Smits.  It is both
capable of negotiating additional capabilities with the server, and also
parses the list of mailboxes on its own.

```
$ echo abc123 | python3 open_imap.py mail.example.com brandon
Capabilities: ('IMAP4REV1', 'LITERAL+', 'SASL-IR', 'LOGIN-REFERRALS',
'ID', 'ENABLE', 'IDLE', 'SORT', 'SORT=DISPLAY', 'THREAD=REFERENCES',
'THREAD=REFS', 'THREAD=ORDEREDSUBJECT', 'MULTIAPPEND', 'URL-PARTIAL',
'CATENATE', 'UNSELECT', 'CHILDREN', 'NAMESPACE', 'UIDPLUS',
'LIST-EXTENDED', 'I18NLEVEL=1', 'CONDSTORE', 'QRESYNC', 'ESEARCH',
'ESORT', 'SEARCHRES', 'WITHIN', 'CONTEXT=SEARCH', 'LIST-STATUS',
'SPECIAL-USE', 'BINARY', 'MOVE')
Listing mailboxes:
  \HasNoChildren                / INBOX
```

Two further scripts show how to pull basic information about a folder,
and how to provide a full summary of the messages inside.

```
$ echo abc123 | python3 folder_info.py mail.example.com brandon INBOX
EXISTS: 3
FLAGS: ('\\Answered', '\\Flagged', '\\Deleted', '\\Seen', '\\Draft')
NOMODSEQ: ['']
PERMANENTFLAGS: ()
READ-ONLY: ['']
RECENT: 0
UIDNEXT: 11
UIDVALIDITY: 1414010141
UNSEEN: ['1']
```

```
$ echo abc123 | python3 folder_summary.py mail.example.com brandon INBOX
1 Administrator <admin@mail.example.com>
   We are happy that you have chosen to use example.com's indus ...
2 Administrator <admin@mail.example.com>
   Administrator e-mails are sent as plain ASCII without MIME o ...
3 Test Sender <sender@example.com>
  Parts: multipart/alternative text/plain
```

The final script, `simple_client.py`, is quite elaborate (despite its
name) and allows the user to interactively visit folders and the
messages inside.
