[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 17<br>FTP

This is a directory of program listings from Chapter 17 of the book:

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

Most of the scripts in this chapter are for searching and downloading
from FTP sites, and are hard-wired to run against well-known public
servers that should give predictable results.

```
$ python3 connect.py
Welcome: 220 ProFTPD Server
Current working directory: /
```

```
$ python3 nlst.py
13 entries:
INDEX
README
ephem_4.28.tar.Z
hawaii_scope
incoming
jupitor-moons.shar.Z
lunar.c.Z
lunisolar.shar.Z
moon.shar.Z
planetary
sat-track.tar.Z
stars.tar.Z
xephem.tar.Z
```

```
$ python3 dir.py
13 entries:
-rw-r--r--   1 48       25         341303 Oct  2  1992 ephem_4.28.tar.Z
drwxr-xr-x   2 48       25           4096 Feb 11  1999 hawaii_scope
drwxr-xr-x   2 48       utempter     4096 Feb 11  1999 incoming
-rw-r--r--   1 48       25            750 Feb 14  1994 INDEX
-rw-r--r--   1 48       25           5983 Oct  2  1992 jupitor-moons.shar.Z
-rw-r--r--   1 48       25           1751 Oct  2  1992 lunar.c.Z
-rw-r--r--   1 48       25           8078 Oct  2  1992 lunisolar.shar.Z
-rw-r--r--   1 48       25          64209 Oct  2  1992 moon.shar.Z
drwxr-xr-x   2 48       25           4096 Jan  6  1993 planetary
-rw-r--r--   1 root     bin           135 Feb 11  1999 README
-rw-r--r--   1 48       25         129969 Oct  2  1992 sat-track.tar.Z
-rw-r--r--   1 48       25          16504 Oct  2  1992 stars.tar.Z
-rw-r--r--   1 48       25         410650 Oct  2  1992 xephem.tar.Z
```

The simple download files are silent while doing their work, and you
will have to list the current directory contents later to see that they
had any effect.  The advanced download scripts, by contrast, should
constantly update the screen as you run them to report on progress.

```
$ python3 asciidl.py
```

```
$ python3 binarydl.py
```

```
$ python3 advbinarydl.py
Received 1448 of 1259161 total bytes (0.1%)
...
Received 1259161 of 1259161 total bytes (100.0%)
```

```
$ python3 recursedl.py
/pub/linux/kernel/Historic/old-versions
/pub/linux/kernel/Historic/old-versions/impure
/pub/linux/kernel/Historic/old-versions/old
/pub/linux/kernel/Historic/old-versions/old/corrupt
/pub/linux/kernel/Historic/old-versions/tytso
```

Finally, the two scripts for doing binary uploads are best run from
inside of the [Playground](../../playground#readme) because it comes
with a host named `ftp.example.com` that already has an FTP server
installed.  Try creating the `h1` host and moving into the `chapter17`
directory:

    $ ./play h1

    # cd py3/chapter17

The username `brandon` and the password `abc123` should let you upload
binary files to the user’s home directory:

```
$ python3 binaryul.py ftp.example.com brandon /bin/true .
Enter password for brandon on ftp.example.com:  abc123
```

```
$ python3 advbinaryul.py ftp.example.com brandon /bin/false .
Enter password for brandon on ftp.example.com:  abc123
Sent 8192 of 27168 bytes (30.2%)
Sent 16384 of 27168 bytes (60.3%)
Sent 24576 of 27168 bytes (90.5%)
Sent 27168 of 27168 bytes (100.0%)
```

A quick connection to the `ftp` host should then confirm that the files
arrived successfully:

    # ssh brandon@ftp.example.com
    brandon@ftp.example.com's password: abc123

    Welcome to Ubuntu 14.04.1 LTS (GNU/Linux 3.13.0-24-generic x86_64)

    $ ls -l
    total 56
    -rw------- 1 brandon brandon   27168 Oct 23 01:47 false
    -rw------- 1 brandon brandon   27168 Oct 23 01:47 true
