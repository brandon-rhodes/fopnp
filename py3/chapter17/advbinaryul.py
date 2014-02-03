#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter17/advbinaryul.py

from ftplib import FTP
import sys, getpass, os.path

BLOCKSIZE = 8192  # chunk size to read and transmit: 8 kB

def main():
    if len(sys.argv) != 5:
        print("usage:", sys.argv[0],
              "<host> <username> <localfile> <remotedir>")
        exit(2)

    host, username, localfile, remotedir = sys.argv[1:]
    prompt = "Enter password for {} on {}: ".format(username, host)
    password = getpass.getpass(prompt)
    ftp = FTP(host)
    ftp.login(username, password)

    ftp.cwd(remotedir)
    ftp.voidcmd("TYPE I")
    datasock, esize = ftp.ntransfercmd('STOR %s' % os.path.basename(localfile))
    size = os.stat(localfile)[6]
    nbytes = 0

    f = open(localfile, 'rb')
    while 1:
        data = f.read(BLOCKSIZE)
        if not data:
            break
        datasock.sendall(data)
        nbytes += len(data)
        print("\rSent", nbytes, "of", size, "bytes",
              "(%.1f%%)\r" % (100 * nbytes / float(size)))
        sys.stdout.flush()

    print()
    datasock.close()
    f.close()
    ftp.voidresp()
    ftp.quit()

if __name__ == '__main__':
    main()
