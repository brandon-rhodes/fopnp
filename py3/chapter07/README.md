[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 7<br>Server Architecture

This is a directory of program listings from Chapter 7 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

This chapter implements the same network service seven different ways.
The seven different servers look pretty much the same when run from the
command line, which is more or less the point.  What is interesting
about them is how differently they are written while yet providing
exactly the same network service.

Any of the server scripts, when run at the command line, let the single
client script — the appropriately named `client.py` — connect and ask a
series of questions to which the server replies with answers.

```
$ python3 srv_single.py '' &>server.log &
```

```
$ python3 client.py localhost
b'Simple is better than?' b'Complex.'
b'Beautiful is better than?' b'Ugly.'
b'Explicit is better than?' b'Implicit.'
```

```
$ cat server.log
Listening at ('', 1060)
Accepted connection from ('127.0.0.1', 41285)
Client socket to ('127.0.0.1', 41285) has closed
```

You can run the `test.sh` script if you want to verify that all seven
work correctly on your platform.  The script will start each of the
servers in turn, and see whether the client can really connect or not.

Two final versions of the Zen-of-Python server require a bit of manual
configuration: the servers that are designed to run under the `inetd`
daemon.  You can try them in the [Playground](../../playground#readme)
on the `ftp.example.com` host, where `inetd` happens to already be
running to provide a Telnet service for the scripts in Chapter 16.  Once
you have the playground running, create a client host like `h1`:

    $ ./play.sh h1

Because each client host auto-mounts the `py3` directory, you will have
access to the scripts and configuration file that need to be copied over
to `ftp.example.com` for the two services to run.  You can perform the
copy using the following commands on host `h1`:

    # cd /py3/chapter07
    # scp in_zen1.py in_zen2.py zen_utils.py ftp.example.com:/
    # scp inetd.conf ftp.example.com:
    # ssh ftp.example.com

Once the `ssh` command has offered you a prompt on the `ftp` machine,
you can run `ps` to verify that `inetd` is indeed running.

    # ps axf
      PID TTY      STAT   TIME COMMAND
    ...
       36 ?        Ss     0:00 /usr/sbin/inetd
    ...

You can add the Zen-of-Python service to its existing list of services,
and get the Python scripts marked publicly readable so that they can be
run as the `brandon` user, by typing:

    # cat inetd.conf >> /etc/inetd.conf
    # /etc/init.d/openbsd-inetd reload
    # chmod a+r /*.py

You can now log back out of the `ftp` host and, from the `h1` host,
connect to the `inetd` powered servers on both of the port numbers
mentioned in `inet.conf`:

    # python3 client.py ftp.example.com -p 1060

    b'Beautiful is better than?' b'Ugly.'
    b'Explicit is better than?' b'Implicit.'
    b'Simple is better than?' b'Complex.'

    # python3 client.py ftp.example.com -p 1061

    b'Beautiful is better than?' b'Ugly.'
    b'Simple is better than?' b'Complex.'
    b'Explicit is better than?' b'Implicit.'

If you later log back in to the `ftp` host, you can view the logs of
both servers.

    # cat /tmp/zen.log
    Accepted connection from ('10.25.1.65', 49327)
    Client socket to ('10.25.1.65', 49327) has closed
