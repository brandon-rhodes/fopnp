#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter15/open_imap.py
# Opening an IMAP connection with the powerful IMAPClient

import getpass, sys
from imapclient import IMAPClient

def main():
    if len(sys.argv) != 3:
        print('usage: %s hostname username' % sys.argv[0])
        sys.exit(2)

    hostname, username = sys.argv[1:]
    c = IMAPClient(hostname, ssl=True)
    try:
        c.login(username, getpass.getpass())
    except c.Error as e:
        print('Could not log in:', e)
    else:
        print('Capabilities:', c.capabilities())
        print('Listing mailboxes:')
        data = c.list_folders()
        for flags, delimiter, folder_name in data:
            print('  %-30s%s %s' % (' '.join(flags), delimiter, folder_name))
    finally:
        c.logout()

if __name__ == '__main__':
    main()
