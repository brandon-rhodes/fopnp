#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 10 - fetch_urllib2.py
# Submitting a form and retrieving a page with urllib2

import urllib, urllib2
data = urllib.urlencode({'inputstring': 'Phoenix, AZ'})
info = urllib2.urlopen('http://forecast.weather.gov/zipcity.php', data)
content = info.read()
open('phoenix.html', 'w').write(content)
