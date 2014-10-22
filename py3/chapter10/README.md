[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 10<br>HTTP Servers

This is a directory of program listings from Chapter 10 of the book:

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
convert them to the older syntax.  Then edit `wsgi_env.py` to remove the
`u` in front of its string literals, because `wsgiref` cannot process
Unicode headers or status codes (whereas `gunicorn`, with which we run
the other example servers, does not seem to have a problem).

The `wsgi_env.py` script is designed to familiarize the reader with what
a live WSGI environment dictionary looks like.  When contacted, it
replies with a pretty-printed version of the dictionary:

```
$ python3 wsgi_env.py &
Serving on 0.0.0.0 port 8000
```

```
$ curl -s http://127.0.0.1:8000/ && echo
127.0.0.1 - - [25/Mar/2014 19:20:08] "GET / HTTP/1.1" 200 3517
Here is the WSGI environment:

{'BASH_ENV': '$HOME/.bashenv',
 'CONDA_DEFAULT_ENV': '/home/brandon/.v/fopnp-py3',
 'CONTENT_LENGTH': '',
 'CONTENT_TYPE': 'text/plain',
 'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-jbCOBCOyCX',
 'DEFAULTS_PATH': '/usr/share/gconf/xfce.default.path',
 'DESKTOP_SESSION': 'xfce',
 'DISPLAY': ':0.0',
 'EDITOR': '/home/brandon/bin/enw',
 'FVWM_MODULEDIR': '/usr/lib/fvwm/2.6.5',
 'FVWM_USERDIR': '/home/brandon/.fvwm',
 'GATEWAY_INTERFACE': 'CGI/1.1',
 'GDMSESSION': 'xfce',
 'GDM_LANG': 'en_US',
 'GLADE_CATALOG_PATH': ':',
 'GLADE_MODULE_PATH': ':',
 'GLADE_PIXMAP_PATH': ':',
 'GNOME_KEYRING_CONTROL': '/run/user/1000/keyring-oSpEEj',
 'GNOME_KEYRING_PID': '1816',
 'GREP_COLOR': '1;32',
 'GREP_OPTIONS': '--color=auto',
 'HOME': '/home/brandon',
 'HOSTDISPLAY': 'guinness:0.0',
 'HTTP_ACCEPT': '*/*',
 'HTTP_HOST': '127.0.0.1:8000',
 'HTTP_USER_AGENT': 'curl/7.35.0',
 'IM_CONFIG_PHASE': '1',
 'INSTANCE': '',
 'JOB': 'dbus',
 'LANG': 'C.UTF-8',
 'LANGUAGE': 'en_US',
 'LC_COLLATE': 'C',
 'LC_CTYPE': 'en_US.UTF-8',
 'LESS': '-i -j.49 -M -R -z-2',
 'LOGNAME': 'brandon',
 'LSCOLORS': 'Gxfxcxdxbxegedabagacad',
 'MANDATORY_PATH': '/usr/share/gconf/xfce.mandatory.path',
 'OLDPWD': '/home/brandon/fopnp/py3',
 'PAGER': 'less',
 'PATH': '/home/brandon/.v/fopnp-py3/bin:/home/brandon/bin:/home/brandon/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
 'PATH_INFO': '/',
 'PIP_DOWNLOAD_CACHE': '/home/brandon/.cache/pip',
 'PWD': '/home/brandon/fopnp/py3/chapter10',
 'PYTHONDONTWRITEBYTECODE': 'PLEASE',
 'PYTHONPATH': '/home/brandon/fopnp/py3/tools/monkeys',
 'QUERY_STRING': '',
 'REMOTE_ADDR': '127.0.0.1',
 'REMOTE_HOST': '',
 'REQUEST_METHOD': 'GET',
 'SCRIPT_NAME': '',
 'SELINUX_INIT': 'YES',
 'SERVER_NAME': 'guinness',
 'SERVER_PORT': '8000',
 'SERVER_PROTOCOL': 'HTTP/1.1',
 'SERVER_SOFTWARE': 'WSGIServer/0.2',
 'SESSION': 'xfce',
 'SESSIONTYPE': '',
 'SESSION_MANAGER': 'local/guinness:@/tmp/.ICE-unix/1959,unix/guinness:/tmp/.ICE-unix/1959',
 'SHELL': '/bin/zsh',
 'SHLVL': '2',
 'SSH_AGENT_LAUNCHER': 'upstart',
 'SSH_AGENT_PID': '1910',
 'SSH_AUTH_SOCK': '/tmp/ssh-DW8Gpm8QY5aS/agent.1908',
 'TERM': 'xterm',
 'TEXTDOMAIN': 'im-config',
 'TEXTDOMAINDIR': '/usr/share/locale/',
 'UPSTART_EVENTS': 'started xsession',
 'UPSTART_INSTANCE': '',
 'UPSTART_JOB': 'startxfce4',
 'UPSTART_SESSION': 'unix:abstract=/com/ubuntu/upstart-session/1000/1828',
 'USER': 'brandon',
 'WINDOWID': '83886114',
 'XAUTHORITY': '/home/brandon/.Xauthority',
 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-xfce:/usr/share/upstart/xdg:/etc/xdg:/etc/xdg',
 'XDG_CURRENT_DESKTOP': 'XFCE',
 'XDG_DATA_DIRS': '/usr/share/xfce:/usr/share/xfce4:/usr/local/share/:/usr/share/:/usr/share',
 'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/brandon',
 'XDG_MENU_PREFIX': 'xfce-',
 'XDG_RUNTIME_DIR': '/run/user/1000',
 'XDG_SEAT': 'seat0',
 'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0',
 'XDG_SESSION_ID': 'c2',
 'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0',
 'XDG_VTNR': '7',
 'XTERM_LOCALE': 'en_US.UTF-8',
 'XTERM_SHELL': '/bin/zsh',
 'XTERM_VERSION': 'XTerm(297)',
 '_': '/home/brandon/.v/fopnp-py3/bin/python3',
 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>,
 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>,
 'wsgi.input': <_io.BufferedReader name=5>,
 'wsgi.multiprocess': False,
 'wsgi.multithread': True,
 'wsgi.run_once': False,
 'wsgi.url_scheme': 'http',
 'wsgi.version': (1, 0)}
```

Note that the `&& echo` command that has been appended to `curl` in all
of these shell command lines is simply there to provide a newline before
your shell prompt displays again, because none of these HTTP responses
include a trailing newline.

The other three scripts in this chapter implement the same tiny WSGI
network service.  One speaks “raw WSGI” per the PEP, while the other two
use third-party libraries that wrap WSGI in pretty request and response
objects.

```
$ gunicorn -b ':8001' timeapp_raw:app &
```

```
$ gunicorn -b ':8002' timeapp_werkz:app &
```

```
$ gunicorn -b ':8003' timeapp_webob:app &
```

```
$ curl -s http://127.0.0.1:8001/ && echo
Wed Oct 22 15:55:54 2014
```

```
$ curl -s http://127.0.0.1:8002/ && echo
Wed Oct 22 15:55:55 2014
```

```
$ curl -s http://127.0.0.1:8003/ && echo
Wed Oct 22 15:55:56 2014
```

The sample network service simply returns the current time.
