#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search2.py

import json
import urllib, urllib.request, urllib.error, urllib.parse

params = {'q': '207 N. Defiance St, Archbold, OH',
          'output': 'json', 'oe': 'utf8'}
url = 'http://maps.google.com/maps/geo?' + urllib.parse.urlencode(params)

rawreply = urllib.request.urlopen(url).read()

reply = json.loads(rawreply.decode('utf-8'))
print(reply['Placemark'][0]['Point']['coordinates'][:-1])
