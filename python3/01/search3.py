#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search3.py

import http.client
import json

path = ('/maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH'
        '&output=json&oe=utf8')

connection = http.client.HTTPConnection('maps.google.com')
connection.request('GET', path)
rawreply = connection.getresponse().read()

reply = json.loads(rawreply.decode('utf-8'))
print(reply['Placemark'][0]['Point']['coordinates'][:-1])
