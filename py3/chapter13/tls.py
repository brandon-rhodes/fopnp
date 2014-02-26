#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter13/tls.py

import sys, smtplib, socket, ssl

message_template = """To: %s
From: %s
Subject: Test Message from simple.py

Hello,

This is a test message sent to you from the tls.py program
in Foundations of Python Network Programming.
"""

def main():
    if len(sys.argv) < 4:
        print("Syntax: %s server fromaddr toaddr [toaddr...]" % sys.argv[0])
        sys.exit(2)

    server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]
    message = message_template % (', '.join(toaddrs), fromaddr)

    try:
        s = smtplib.SMTP(server)
        send_message_securely(s, fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print(" *** Your message may not have been sent!")
        print(e)
        sys.exit(1)
    else:
        print("Message successfully sent to %d recipient(s)" % len(toaddrs))
        s.quit()

def send_message_securely(s, fromaddr, toaddrs, message):
    code = s.ehlo()[0]
    uses_esmtp = (200 <= code <= 299)
    if not uses_esmtp:
        code = s.helo()[0]
        if not (200 <= code <= 299):
            print("Remove server refused HELO; code:", code)
            sys.exit(1)

    if uses_esmtp and s.has_extn('starttls'):
        print("Negotiating TLS....")
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.set_default_verify_paths()
        context.verify_mode = ssl.CERT_REQUIRED
        s.starttls(context=context)
        code = s.ehlo()[0]
        if not (200 <= code <= 299):
            print("Couldn't EHLO after STARTTLS")
            sys.exit(5)
        print("Using TLS connection.")
    else:
        print("Server does not support TLS; using normal connection.")

    s.sendmail(fromaddr, toaddrs, message)

if __name__ == '__main__':
    main()
