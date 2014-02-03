#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter15/folder_info.py
# Opening an IMAP connection with IMAPClient and listing folder information.

import getpass, sys
from imapclient import IMAPClient

def main():
    try:
        hostname, username = sys.argv[1:]
    except ValueError:
        print('usage: %s hostname username' % sys.argv[0])
        sys.exit(2)

    c = IMAPClient(hostname, ssl=True)
    try:
        c.login(username, getpass.getpass())
    except c.Error as e:
        print('Could not log in:', e)
        sys.exit(1)
    else:
        select_dict = c.select_folder('INBOX', readonly=True)
        for k, v in list(select_dict.items()):
            print('%s: %r' % (k, v))
        c.logout()

if __name__ == '__main__':
    main()
