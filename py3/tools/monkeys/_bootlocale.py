# If you scroll down you will see that this is not merely a cut and
# paste of the usual contents of the _bootlocale.py file, but a way to
# set up the state of Python so that the code examples in each chapter
# README always run the same way.

"""A minimal subset of the locale module used at interpreter startup
(imported by the _io module), in order to reduce startup time.

Don't import directly from third-party code; use the `locale` module instead!
"""
import sys
import _locale

if sys.platform.startswith("win"):
    def getpreferredencoding(do_setlocale=True):
        return _locale._getdefaultlocale()[1]
else:
    try:
        _locale.CODESET
    except AttributeError:
        def getpreferredencoding(do_setlocale=True):
            # This path for legacy systems needs the more complex
            # getdefaultlocale() function, import the full locale module.
            import locale
            return locale.getpreferredencoding(do_setlocale)
    else:
        def getpreferredencoding(do_setlocale=True):
            assert not do_setlocale
            result = _locale.nl_langinfo(_locale.CODESET)
            if not result and sys.platform == 'darwin':
                # nl_langinfo can return an empty string
                # when the setting has an invalid value.
                # Default to UTF-8 in that case because
                # UTF-8 is the default charset on OSX and
                # returning nothing will crash the
                # interpreter.
                result = 'UTF-8'
            return result

# ADDED FOR FOUNDATIONS OF NETWORK PROGRAMMING session.txt REPRODUCABILITY:

# Stabilize the random number generator so that various UUID functions
# always return the same value.

import random
random.seed(0)
del random

# Set the current time so that messages built with the "email" library
# have a stable "Date:" field.

import time as time_module
def time():
    return 1395789608.667911
time_module.time = time
del time

# Stabilize the current process PID so that "Message-ID:" fields stay
# the same.

import os
def getpid():
    return 15748
os.getpid = getpid
del getpid
del os

# Accept passwords from standard input instead of looking for the
# controlling terminal.

import getpass
def fake_getpass(prompt='Password: '):
    print(prompt, 'abc123')
    return 'abc123'
getpass.getpass = fake_getpass
del getpass
del fake_getpass

# Replace print() with pretty-print when scripts print raw data
# structures, so that dictionary keys come out in a stable order.

from pprint import pprint
builtin_print = print

def print(*args, **kw):
    if len(args) == 1 and not isinstance(args[0], str):
        return pprint(args[0])
    return builtin_print(*args, **kw)

__builtins__['print'] = print
del print
