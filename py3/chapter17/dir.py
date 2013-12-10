#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter17/dir.py

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
