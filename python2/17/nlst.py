#!/usr/bin/env python
# NLST example - Chapter 17 - nlst.py

from ftplib import FTP

f = FTP('ftp.ibiblio.org')
f.login()
f.cwd('/pub/academic/astronomy/')
entries = f.nlst()
entries.sort()
print len(entries), "entries:"
for entry in entries:
    print entry
f.quit()
