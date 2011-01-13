#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search1.py

from googlemaps import GoogleMaps
address = '207 N. Defiance St, Archbold, OH'
print GoogleMaps().address_to_latlng(address)
