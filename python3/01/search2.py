#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search2.py

import urllib, urllib2
try:
    import json
except ImportError:  # for Python 2.5
    import simplejson as json

params = {'q': '207 N. Defiance St, Archbold, OH',
          'output': 'json', 'oe': 'utf8'}
url = 'http://maps.google.com/maps/geo?' + urllib.urlencode(params)

rawreply = urllib2.urlopen(url).read()

reply = json.loads(rawreply)
print reply['Placemark'][0]['Point']['coordinates'][:-1]
