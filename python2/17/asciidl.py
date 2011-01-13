#!/usr/bin/env python
# ASCII download - Chapter 17 - asciidl.py
# Downloads README from remote and writes it to disk.

import os
from ftplib import FTP

if os.path.exists('README'):
    raise IOError('refusing to overwrite your README file')

def writeline(data):
    fd.write(data)
    fd.write(os.linesep)

f = FTP('ftp.kernel.org')
f.login()
f.cwd('/pub/linux/kernel')

fd = open('README', 'w')
f.retrlines('RETR README', writeline)
fd.close()

f.quit()
