#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 1 - search1.py

from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)
