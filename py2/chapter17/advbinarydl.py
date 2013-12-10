#!/usr/bin/env python
# Advanced binary download - Chapter 17 - advbinarydl.py

import os, sys
from ftplib import FTP

if os.path.exists('linux-1.0.tar.gz'):
    raise IOError('refusing to overwrite your linux-1.0.tar.gz file')

f = FTP('ftp.kernel.org')
f.login()

f.cwd('/pub/linux/kernel/v1.0')
f.voidcmd("TYPE I")

datasock, size = f.ntransfercmd("RETR linux-1.0.tar.gz")
bytes_so_far = 0
fd = open('linux-1.0.tar.gz', 'wb')

while 1:
    buf = datasock.recv(2048)
    if not buf:
        break
    fd.write(buf)
    bytes_so_far += len(buf)
    print "\rReceived", bytes_so_far,
    if size:
        print "of %d total bytes (%.1f%%)" % (
            size, 100 * bytes_so_far / float(size)),
    else:
        print "bytes",
    sys.stdout.flush()

print
fd.close()
datasock.close()
f.voidresp()
f.quit()
