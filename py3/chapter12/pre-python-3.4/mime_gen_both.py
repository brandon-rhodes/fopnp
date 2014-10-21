#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/pre-python-3.4/mime_gen_both.py

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import utils, encoders
import mimetypes, sys

def build_part(data, contenttype):
    maintype, subtype = contenttype.split('/')
    if maintype == 'text':
        part = MIMEText(data, _subtype=subtype)
    else:
        part = MIMEBase(maintype, subtype)
        part.set_payload(data)
        encoders.encode_base64(part)
    return part

def build_attachment(filename):
    mimetype, mimeencoding = mimetypes.guess_type(filename)
    if mimeencoding or (mimetype is None):
        mimetype = 'application/octet-stream'
    mode = 'r' if mimetype.startswith('text/') else 'rb'
    with open(filename, mode) as fd:
        part = build_part(fd.read(), mimetype)
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    return part

messagetext = """Hello,

This is a *great* test message from Chapter 12.  I hope you enjoy it!

-- Anonymous"""
messagehtml = """Hello,<P>
This is a <B>great</B> test message from Chapter 12.  I hope you enjoy
it!<P>
-- <I>Anonymous</I>"""

msg = MIMEMultipart()
msg['To'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 12'
msg['Date'] = utils.formatdate(localtime = 1)
msg['Message-ID'] = utils.make_msgid()

body = MIMEMultipart('alternative')
body.attach(build_part(messagetext, 'text/plain'))
body.attach(build_part(messagehtml, 'text/html'))
msg.attach(body)

for filename in sys.argv[1:]:
    msg.attach(build_attachment(filename))
print(msg.as_string())
