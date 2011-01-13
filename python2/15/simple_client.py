#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 15 - simple_client.py
# Letting a user browse folders, messages, and message parts.

import getpass, sys
from imapclient import IMAPClient

try:
    hostname, username = sys.argv[1:]
except ValueError:
    print 'usage: %s hostname username' % sys.argv[0]
    sys.exit(2)

banner = '-' * 72

c = IMAPClient(hostname, ssl=True)
try:
    c.login(username, getpass.getpass())
except c.Error, e:
    print 'Could not log in:', e
    sys.exit(1)

def display_structure(structure, parentparts=[]):
    """Attractively display a given message structure."""

    # The whole body of the message is named 'TEXT'.

    if parentparts:
        name = '.'.join(parentparts)
    else:
        print 'HEADER'
        name = 'TEXT'

    # Print this part's designation and its MIME type.

    is_multipart = isinstance(structure[0], list)
    if is_multipart:
        parttype = 'multipart/%s' % structure[1].lower()
    else:
        parttype = ('%s/%s' % structure[:2]).lower()
    print '%-9s' % name, parttype,

    # For a multipart part, print all of its subordinate parts; for
    # other parts, print their disposition (if available).

    if is_multipart:
        print
        subparts = structure[0]
        for i in range(len(subparts)):
            display_structure(subparts[i], parentparts + [ str(i + 1) ])
    else:
        if structure[6]:
            print 'size=%s' % structure[6],
        if structure[8]:
            disposition, namevalues = structure[8]
            print disposition,
            for i in range(0, len(namevalues), 2):
                print '%s=%r' % namevalues[i:i+2]
        print

def explore_message(c, uid):
    """Let the user view various parts of a given message."""

    msgdict = c.fetch(uid, ['BODYSTRUCTURE', 'FLAGS'])

    while True:
        print
        print 'Flags:',
        flaglist = msgdict[uid]['FLAGS']
        if flaglist:
            print ' '.join(flaglist)
        else:
            print 'none'
        display_structure(msgdict[uid]['BODYSTRUCTURE'])
        print
        reply = raw_input('Message %s - type a part name, or "q" to quit: '
                          % uid).strip()
        print
        if reply.lower().startswith('q'):
            break
        key = 'BODY[%s]' % reply
        try:
            msgdict2 = c.fetch(uid, [key])
        except c._imap.error:
            print 'Error - cannot fetch section %r' % reply
        else:
            content = msgdict2[uid][key]
            if content:
                print banner
                print content.strip()
                print banner
            else:
                print '(No such section)'

def explore_folder(c, name):
    """List the messages in folder `name` and let the user choose one."""

    while True:
        c.select_folder(name, readonly=True)
        msgdict = c.fetch('1:*', ['BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)]',
                                  'FLAGS', 'INTERNALDATE', 'RFC822.SIZE'])
        print
        for uid in sorted(msgdict):
            items = msgdict[uid]
            print '%6d  %20s  %6d bytes  %s' % (
                uid, items['INTERNALDATE'], items['RFC822.SIZE'],
                ' '.join(items['FLAGS']))
            for i in items['BODY[HEADER.FIELDS (FROM SUBJECT)]'].splitlines():
                print ' ' * 6, i.strip()

        reply = raw_input('Folder %s - type a message UID, or "q" to quit: '
                          % name).strip()
        if reply.lower().startswith('q'):
            break
        try:
            reply = int(reply)
        except ValueError:
            print 'Please type an integer or "q" to quit'
        else:
            if reply in msgdict:
                explore_message(c, reply)

    c.close_folder()

def explore_account(c):
    """Display the folders in this IMAP account and let the user choose one."""

    while True:

        print
        folderflags = {}
        data = c.list_folders()
        for flags, delimiter, name in data:
            folderflags[name] = flags
        for name in sorted(folderflags.keys()):
            print '%-30s %s' % (name, ' '.join(folderflags[name]))
        print

        reply = raw_input('Type a folder name, or "q" to quit: ').strip()
        if reply.lower().startswith('q'):
            break
        if reply in folderflags:
            explore_folder(c, reply)
        else:
            print 'Error: no folder named', repr(reply)

if __name__ == '__main__':
    explore_account(c)
