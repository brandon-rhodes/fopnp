#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter13/ehlo.py

import smtplib, socket, sys

message_template = """To: %s
From: %s
Subject: Test Message from simple.py

Hello,

This is a test message sent to you from the ehlo.py program
in Foundations of Python Network Programming.
"""

def main():
    if len(sys.argv) < 4:
        print("usage: %s server fromaddr toaddr [toaddr...]" % sys.argv[0])
        sys.exit(2)

    server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]
    message = message_template % (', '.join(toaddrs), fromaddr)

    try:
        s = smtplib.SMTP(server)
        report_on_message_size(s, fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print(" *** Your message may not have been sent!")
        print(e)
        sys.exit(1)
    else:
        print("Message successfully sent to %d recipient(s)" % len(toaddrs))
        s.quit()

def report_on_message_size(s, fromaddr, toaddrs, message):
    code = s.ehlo()[0]
    uses_esmtp = (200 <= code <= 299)
    if not uses_esmtp:
        code = s.helo()[0]
        if not (200 <= code <= 299):
            print("Remote server refused HELO; code:", code)
            sys.exit(1)

    if uses_esmtp and s.has_extn('size'):
        print("Maximum message size is", s.esmtp_features['size'])
        if len(message) > int(s.esmtp_features['size']):
            print("Message too large; aborting.")
            sys.exit(1)

    s.sendmail(fromaddr, toaddrs, message)

if __name__ == '__main__':
    main()
