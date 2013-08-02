#!/usr/bin/env python3
# ASCII download - Chapter 17 - asciidl.py
# Downloads README from remote and writes it to disk.

import os
from ftplib import FTP

if os.path.exists('README'):
    raise IOError('refusing to overwrite your README file')

ftp = FTP('ftp.kernel.org')
ftp.login()
ftp.cwd('/pub/linux/kernel')

with open('README', 'w') as f:
    def writeline(data):
        f.write(data)
        f.write(os.linesep)

    ftp.retrlines('RETR README', writeline)

ftp.quit()
