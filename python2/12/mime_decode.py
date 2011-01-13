#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 12 - mime_decode.py
# This program requires Python 2.2.2 or above

import sys, email
counter = 0
parts = []

def printmsg(msg, level = 0):
    global counter
    l = "|  " * level
    if msg.is_multipart():
        print l + "Found multipart:"
        for item in msg.get_payload():
            printmsg(item, level + 1)
    else:
        disp = ['%d. Decodable part' % (counter + 1)]
        if 'content-type' in msg:
            disp.append(msg['content-type'])
        if 'content-disposition' in msg:
            disp.append(msg['content-disposition'])
        print l + ", ".join(disp)
        counter += 1
        parts.append(msg)

inputfd = open(sys.argv[1])
msg = email.message_from_file(inputfd)
printmsg(msg)

while 1:
    print "Select part number to decode or q to quit: "
    part = sys.stdin.readline().strip()
    if part == 'q':
        sys.exit(0)
    try:
        part = int(part)
        msg = parts[part - 1]
    except:
        print "Invalid selection."
        continue

    print "Select file to write to:"
    filename = sys.stdin.readline().strip()
    try:
        fd = open(filename, 'wb')
    except:
        print "Invalid filename."
        continue

    fd.write(msg.get_payload(decode = 1))
