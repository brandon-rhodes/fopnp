#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter15/simple_client.py
# Letting a user browse folders, messages, and message parts.

import getpass, sys
from imapclient import IMAPClient

banner = '-' * 72

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
        explore_account(c)
    finally:
        c.logout()

def explore_account(c):
    """Display the folders in this IMAP account and let the user choose one."""

    while True:

        print()
        folderflags = {}
        data = c.list_folders()
        for flags, delimiter, name in data:
            folderflags[name] = flags
        for name in sorted(folderflags.keys()):
            print('%-30s %s' % (name, ' '.join(folderflags[name])))
        print()

        reply = input('Type a folder name, or "q" to quit: ').strip()
        if reply.lower().startswith('q'):
            break
        if reply in folderflags:
            explore_folder(c, reply)
        else:
            print('Error: no folder named', repr(reply))

def explore_folder(c, name):
    """List the messages in folder `name` and let the user choose one."""

    while True:
        c.select_folder(name, readonly=True)
        msgdict = c.fetch('1:*', ['BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)]',
                                  'FLAGS', 'INTERNALDATE', 'RFC822.SIZE'])
        print()
        for uid in sorted(msgdict):
            items = msgdict[uid]
            print('%6d  %20s  %6d bytes  %s' % (
                uid, items['INTERNALDATE'], items['RFC822.SIZE'],
                ' '.join(items['FLAGS'])))
            for i in items['BODY[HEADER.FIELDS (FROM SUBJECT)]'].splitlines():
                print(' ' * 6, i.strip())

        reply = input('Folder %s - type a message UID, or "q" to quit: '
                          % name).strip()
        if reply.lower().startswith('q'):
            break
        try:
            reply = int(reply)
        except ValueError:
            print('Please type an integer or "q" to quit')
        else:
            if reply in msgdict:
                explore_message(c, reply)

    c.close_folder()

def explore_message(c, uid):
    """Let the user view various parts of a given message."""

    msgdict = c.fetch(uid, ['BODYSTRUCTURE', 'FLAGS'])

    while True:
        print()
        print('Flags:', end=' ')
        flaglist = msgdict[uid]['FLAGS']
        if flaglist:
            print(' '.join(flaglist))
        else:
            print('none')
        print('Structure:')
        display_structure(msgdict[uid]['BODYSTRUCTURE'])
        print()
        reply = input('Message %s - type a part name, or "q" to quit: '
                          % uid).strip()
        print()
        if reply.lower().startswith('q'):
            break
        key = 'BODY[%s]' % reply
        try:
            msgdict2 = c.fetch(uid, [key])
        except c._imap.error:
            print('Error - cannot fetch section %r' % reply)
        else:
            content = msgdict2[uid][key]
            if content:
                print(banner)
                print(content.strip())
                print(banner)
            else:
                print('(No such section)')

def display_structure(structure, parentparts=[]):
    """Attractively display a given message structure."""

    # The whole body of the message is named 'TEXT'.

    if parentparts:
        name = '.'.join(parentparts)
    else:
        print('  HEADER')
        name = 'TEXT'

    # Print a simple, non-multipart MIME part.  Include its disposition,
    # if available.

    is_multipart = not isinstance(structure[0], str)

    if not is_multipart:
        parttype = ('%s/%s' % structure[:2]).lower()
        print('  %-9s' % name, parttype, end=' ')
        if structure[6]:
            print('size=%s' % structure[6], end=' ')
        if structure[9]:
            print('disposition=%s' % structure[9][0],
                  ' '.join('{}={}'.format(k, v) for k, v in structure[9][1:]),
                  end=' ')
        print()
        return

    # For a multipart part, print all of its subordinate parts.

    parttype = 'multipart/%s' % structure[1].lower()
    print('  %-9s' % name, parttype, end=' ')
    print()
    subparts = structure[0]
    for i in range(len(subparts)):
        display_structure(subparts[i], parentparts + [ str(i + 1) ])

if __name__ == '__main__':
    main()
