#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter17/advbinarydl.py

import os, sys
from ftplib import FTP

def main():
    if os.path.exists('linux-1.0.tar.gz'):
        raise IOError('refusing to overwrite your linux-1.0.tar.gz file')

    ftp = FTP('ftp.kernel.org')
    ftp.login()
    ftp.cwd('/pub/linux/kernel/v1.0')
    ftp.voidcmd("TYPE I")

    socket, size = ftp.ntransfercmd("RETR linux-1.0.tar.gz")
    nbytes = 0

    f = open('linux-1.0.tar.gz', 'wb')

    while True:
        data = socket.recv(2048)
        if not data:
            break
        f.write(data)
        nbytes += len(data)
        print("\rReceived", nbytes, end=' ')
        if size:
            print("of %d total bytes (%.1f%%)"
                  % (size, 100 * nbytes / float(size)), end=' ')
        else:
            print("bytes", end=' ')
        sys.stdout.flush()

    print()
    f.close()
    socket.close()
    ftp.voidresp()
    ftp.quit()

if __name__ == '__main__':
    main()
