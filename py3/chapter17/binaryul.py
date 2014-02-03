#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter17/binaryul.py

from ftplib import FTP
import sys, getpass, os.path

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
    with open(localfile, 'rb') as f:
        ftp.storbinary('STOR %s' % os.path.basename(localfile), f)
    ftp.quit()

if __name__ == '__main__':
    main()
