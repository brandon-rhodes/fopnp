#!/usr/bin/env python3
# Basic connection - Chapter 17 - connect.py

from ftplib import FTP

ftp = FTP('ftp.ibiblio.org')
print("Welcome:", ftp.getwelcome())
ftp.login()
print("Current working directory:", ftp.pwd())
ftp.quit()
