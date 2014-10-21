#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter12/pre-python-3.4/mime_gen_alt.py

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import utils, encoders

def build_alternative(data, contenttype):
    maintype, subtype = contenttype.split('/')
    if maintype == 'text':
        part = MIMEText(data, _subtype=subtype)
    else:
        part = MIMEBase(maintype, subtype)
        part.set_payload(data)
        encoders.encode_base64(part)
    return part

messagetext = """Hello,

This is a *great* test message from Chapter 12.  I hope you enjoy it!

-- Anonymous"""
messagehtml = """Hello,<P>
This is a <B>great</B> test message from Chapter 12.  I hope you enjoy
it!<P>
-- <I>Anonymous</I>"""


msg = MIMEMultipart('alternative')
msg['To'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 12'
msg['Date'] = utils.formatdate(localtime = 1)
msg['Message-ID'] = utils.make_msgid()

msg.attach(build_alternative(messagetext, 'text/plain'))
msg.attach(build_alternative(messagehtml, 'text/html'))
print(msg.as_string())
