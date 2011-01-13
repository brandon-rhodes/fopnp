#!/usr/bin/env python
# dir() example - Chapter 17 - dir.py

from ftplib import FTP

f = FTP('ftp.ibiblio.org')
f.login()
f.cwd('/pub/academic/astronomy/')
entries = []
f.dir(entries.append)
print "%d entries:" % len(entries)
for entry in entries:
    print entry
f.quit()
