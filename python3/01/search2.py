#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 1 - search2.py

import json
from urllib.parse import urlencode
from urllib.request import urlopen

def geocode(address):
    params = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json?'
    url = base + urlencode(params)
    raw_reply = urlopen(url).read()
    reply = json.loads(raw_reply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
