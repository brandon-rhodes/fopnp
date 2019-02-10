#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search3.py

# (The Google API originally used in this example now requires API keys,
#  so here's an alternative that calls openstreetmap.org.)

import http.client
import json
from urllib.parse import quote_plus

base = '/search'

def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Foundations of Python Network Programming example search3.py'
    headers = {b'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply[0]['lat'], reply[0]['lon'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
