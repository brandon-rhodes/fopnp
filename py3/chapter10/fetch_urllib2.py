#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter10/fetch_urllib2.py
# Submitting a form and retrieving a page with urllib2

import urllib, urllib.request, urllib.error, urllib.parse
data = urllib.parse.urlencode({'inputstring': 'Phoenix, AZ'}).encode('ascii')
info = urllib.request.urlopen('http://forecast.weather.gov/zipcity.php', data)
content = info.read()
open('phoenix.html', 'wb').write(content)
