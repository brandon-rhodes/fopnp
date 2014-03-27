#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/mime_gen_alt.py

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import utils, encoders

message_text = """Hello,

This is a test message from Chapter 12.

 - Anonymous"""

message_html = """<p>Hello,</p>
<p>This is a <b>test message</b> from Chapter 12.</p>
<p> - <i>Anonymous</i></p>"""

def build_alternative(data, contenttype):
    maintype, subtype = contenttype.split('/')
    if maintype == 'text':
        part = MIMEText(data, _subtype=subtype)
    else:
        part = MIMEBase(maintype, subtype)
        part.set_payload(data)
        encoders.encode_base64(part)
    return part

def main():
    msg = MIMEMultipart('alternative')
    msg['To'] = 'recipient@example.com'
    msg['From'] = 'Test Sender <sender@example.com>'
    msg['Subject'] = 'Test Message, Chapter 12'
    msg['Date'] = utils.formatdate(localtime = 1)
    msg['Message-ID'] = utils.make_msgid()

    msg.attach(build_alternative(message_text, 'text/plain'))
    msg.attach(build_alternative(message_html, 'text/html'))
    print(msg.as_string())

if __name__ == '__main__':
    main()
