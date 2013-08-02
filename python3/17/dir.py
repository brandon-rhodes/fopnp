#!/usr/bin/env python3
# dir() example - Chapter 17 - dir.py

from ftplib import FTP

ftp = FTP('ftp.ibiblio.org')
ftp.login()
ftp.cwd('/pub/academic/astronomy/')
entries = []
ftp.dir(entries.append)
ftp.quit()

print(len(entries), "entries:")
for entry in entries:
    print(entry)
