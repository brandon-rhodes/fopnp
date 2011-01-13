#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - fabfile.py
# A sample Fabric script

# Even though this chapter will not cover Fabric, you might want to try
# using Fabric to automate your SSH commands instead of re-inventing the
# wheel.  Here is a script that checks for Python on remote machines.
# Fabric finds this "fabfile.py" automatically if you are in the same
# directory.  Try running both verbosely, and with most messages off:
#
#   $ fab versions:host=server.example.com
#   $ fab --hide=everything versions:host=server.example.com

from fabric.api import *

def versions():
    with cd('/usr/bin'):
        with settings(hide('warnings'), warn_only=True):
            for version in '2.4', '2.5', '2.6', '2.7', '3.0', '3.1':
                result = run('python%s -c "None"' % version)
                if not result.failed:
                    print "Host", env.host, "has Python", version
