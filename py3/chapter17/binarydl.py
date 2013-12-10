#!/usr/bin/env python3
# Binary upload - Chapter 17 - binarydl.py

import os
from ftplib import FTP

if os.path.exists('patch8.gz'):
    raise IOError('refusing to overwrite your patch8.gz file')

ftp = FTP('ftp.kernel.org')
ftp.login()
ftp.cwd('/pub/linux/kernel/v1.0')
with open('patch8.gz', 'wb') as f:
    ftp.retrbinary('RETR patch8.gz', f.write)
ftp.quit()
