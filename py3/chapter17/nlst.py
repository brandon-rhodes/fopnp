#!/usr/bin/env python3
# NLST example - Chapter 17 - nlst.py

from ftplib import FTP

ftp = FTP('ftp.ibiblio.org')
ftp.login()
ftp.cwd('/pub/academic/astronomy/')
entries = ftp.nlst()
ftp.quit()

print(len(entries), "entries:")
for entry in sorted(entries):
    print(entry)
