#!/usr/bin/env python
# Advanced binary upload - Chapter 17 - advbinaryul.py

from ftplib import FTP
import sys, getpass, os.path

BLOCKSIZE = 8192  # chunk size to read and transmit: 8 kB

if len(sys.argv) != 5:
    print "usage: %s <host> <username> <localfile> <remotedir>" % (
        sys.argv[0])
    exit(2)

host, username, localfile, remotedir = sys.argv[1:]
password = getpass.getpass("Enter password for %s on %s: " % \
        (username, host))
f = FTP(host)
f.login(username, password)

f.cwd(remotedir)
f.voidcmd("TYPE I")

fd = open(localfile, 'rb')
datasock, esize = f.ntransfercmd('STOR %s' % os.path.basename(localfile))
size = os.stat(localfile)[6]
bytes_so_far = 0

while 1:
    buf = fd.read(BLOCKSIZE)
    if not buf:
        break
    datasock.sendall(buf)
    bytes_so_far += len(buf)
    print "\rSent", bytes_so_far, "of", size, "bytes", \
        "(%.1f%%)\r" % (100 * bytes_so_far / float(size))
    sys.stdout.flush()

print
datasock.close()
fd.close()
f.voidresp()
f.quit()
