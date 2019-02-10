#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search1.py

# (The Google API originally used in this example now requires API keys,
#  so here's an alternative that calls openstreetmap.org.)

from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    user_agent = 'Foundations of Python Network Programming example search1.py'
    location = Nominatim(user_agent=user_agent).geocode(address)
    print(location.latitude, location.longitude)
