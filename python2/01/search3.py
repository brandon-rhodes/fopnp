#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search3.py

import httplib
try:
    import json
except ImportError:  # for Python 2.5
    import simplejson as json

path = ('/maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH'
        '&output=json&oe=utf8')

connection = httplib.HTTPConnection('maps.google.com')
connection.request('GET', path)
rawreply = connection.getresponse().read()

reply = json.loads(rawreply)
print reply['Placemark'][0]['Point']['coordinates'][:-1]
