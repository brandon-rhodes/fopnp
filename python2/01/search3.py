#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search3.py

import httplib
try:
    import json
except ImportError:  # for Python 2.5
    import simplejson as json

path = ('/maps/api/geocode/json?sensor=false'
        '&address=207+N.+Defiance+St%2C+Archbold%2C+OH')

connection = httplib.HTTPConnection('maps.google.com')
connection.request('GET', path)
rawreply = connection.getresponse().read()

reply = json.loads(rawreply)
print reply['results'][0]['geometry']['location']

# => {u'lat': 41.521954, u'lng': -84.306691}
