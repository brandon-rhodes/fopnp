#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter17/asciidl.py
# Downloads README from remote and writes it to disk.

import os
from ftplib import FTP

def main():
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

if __name__ == '__main__':
    main()
