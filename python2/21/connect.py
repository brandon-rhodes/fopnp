#!/usr/bin/env python
# Basic connection - Chapter 21 - connect.py

from ftplib import FTP

f = FTP('ftp.ibiblio.org')
print "Welcome:", f.getwelcome()
f.login()

print "Current working directory:", f.pwd()
f.quit()
