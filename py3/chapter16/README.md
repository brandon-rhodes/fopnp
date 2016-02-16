[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 16<br>Telnet and SSH

This is a directory of program listings from Chapter 16 of the book:

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

Before diving into Telnet and SSH, the chapter introduces a small shell
program `shell.py` that interprets nothing but whitespace as special on
the command line, in an attempt to demonstrate to the skeptical reader
that all of the characters they are used to treating as special are in
fact quite ordinary down at the level of the operating system.

Once the reader has been instructed as to the role of command lines, the
features of terminals, and the pitfalls of special characters and
quoting, two scripts are introduced which use the old insecure Telnet
protocol.  They can be exercised in the Playground against the
`ftp.example.com` server which, just for fun, has a Telnet server
running as well.

```
$ python3 telnet_login.py ftp.example.com brandon
exec uptime
21:18:15 up  5:40,  1 user,  load average: 0.00, 0.02, 0.05
```

```
$ python3 telnet_codes.py ftp.example.com brandon
Sending terminal type "mypython"
('Will not', 32)
('Will not', 35)
('Will not', 39)
('Do not', 3)
('Will not', 1)
('Will not', 31)
('Do not', 5)
('Will not', 33)
('Do not', 3)
('Do not', 1)
exec echo My terminal type is $TERM
My terminal type is mypython
```

When running the SSH scripts, you can target any of the hosts running in
the Playground — they are all running SSH and should have both a `root`
user and `brandon` user.  For the examples below we will use the latter.
To avoid having to edit the program listings to provide a password
argument to `client.connect()`, ask SSH to install the `root` identity
under the `brandon` account to which you wish to connect.  Because
Docker does not launch your initial shell on a host with everything set
up as though you had logged in, this will only work if you `su` to the
`root` user first:

    $ ./play.sh h1

    # su root

    # ssh-copy-id brandon@www.example.com

By entering the `brandon` password `abc123` the ID should be copied
successfully and a plain SSH command should then succeed without a
password:

    # ssh brandon@www.example.com echo Success
    Success

Once `ssh` itself is working without a password, the Python scripts
should succeed as well.

```
$ python3 ssh_simple.py www.example.com brandon
Welcome to Ubuntu 14.04.1 LTS (GNU/Linux 3.13.0-24-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
Last login: Wed Oct 22 21:38:21 2014 from modema
echo Hello, world
exit
$ Hello, world
$ 
```

As you can see, trying to speak over a single communications channel to
both a shell and the programs it invokes is something of a disaster.
The book explains a better approach:

```
$ python3 ssh_commands.py www.example.com brandon
b'Hello, world!\n'
b'Linux\n'
b' 21:38:33 up  6:00,  0 users,  load average: 0.16, 0.05, 0.06\n'
```

The ability of SSH to support several channels even allows multiple
Python threads to have remove commands running at the same time.

```
$ python3 ssh_threads.py www.example.com brandon
One
A
B
Two
Three
C
```

Finally, SSH includes a built-in file transfer protocol SFTP.

```
$ python3 sftp_get.py www.example.com brandon /etc/lsb-release
Transfer of '/etc/lsb-release' is at 105/105 bytes (100.0%)
Transfer of '/etc/lsb-release' is at 105/105 bytes (100.0%)
```

