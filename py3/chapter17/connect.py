#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter17/connect.py

from ftplib import FTP

ftp = FTP('ftp.ibiblio.org')
print("Welcome:", ftp.getwelcome())
ftp.login()
print("Current working directory:", ftp.pwd())
ftp.quit()
