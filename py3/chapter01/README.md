[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# Chapter 1<br>Introduction to Client-Server Networking

This is a directory of program listings from Chapter 1 of the book:

<dl>
<dt><i>Foundations of Python Network Programming</i></dt>
<dd>
Third Edition, October 2014<br>
by Brandon Rhodes and John Goerzen
</dd>
</dl>

You can learn more about the book by visiting the
[root of this GitHub source code repository](https://github.com/brandon-rhodes/fopnp#readme).

All the scripts in this chapter have been tested successfully under
Python 2.  Simply use [3to2](https://pypi.python.org/pypi/3to2) to
convert them to the older syntax.

The four scripts in this chapter with “search” in their name perform
exactly the same Google geocoding query, but at four different levels of
abstraction in the network protocol hierarchy. This lets the chapter
launch an introduction of each level that the book will be discussing.

```
$ python3 search1.py
(41.521954, -84.306691)
```

```
$ python3 search2.py
{'lat': 41.521954, 'lng': -84.306691}
```

```
$ python3 search3.py
{'lat': 41.521954, 'lng': -84.306691}
```

```
$ python3 search4.py
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Date: Tue, 21 Oct 2014 22:50:21 GMT
Expires: Wed, 22 Oct 2014 22:50:21 GMT
Cache-Control: public, max-age=86400
Vary: Accept-Language
Access-Control-Allow-Origin: *
Server: mafe
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Alternate-Protocol: 80:quic,p=0.01
Connection: close

{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "207",
               "short_name" : "207",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "North Defiance Street",
               "short_name" : "N Defiance St",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Archbold",
               "short_name" : "Archbold",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "German",
               "short_name" : "German",
               "types" : [ "administrative_area_level_3", "political" ]
            },
            {
               "long_name" : "Fulton County",
               "short_name" : "Fulton County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Ohio",
               "short_name" : "OH",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "43502",
               "short_name" : "43502",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "207 North Defiance Street, Archbold, OH 43502, USA",
         "geometry" : {
            "location" : {
               "lat" : 41.521954,
               "lng" : -84.306691
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 41.5233029802915,
                  "lng" : -84.3053420197085
               },
               "southwest" : {
                  "lat" : 41.5206050197085,
                  "lng" : -84.30803998029151
               }
            }
         },
         "types" : [ "street_address" ]
      }
   ],
   "status" : "OK"
}

```

The remaining two scripts are quite tiny. The first shows how a
hostname is turned into an IP address, and the second illustrates the
basic string decoding and encoding maneuvers that Python 3 is careful to
require of network programmers.

```
$ python3 getname.py
The IP address of maps.google.com is 74.125.228.105
```

```
$ python3 stringcodes.py && cat eagle.txt
'413 is in.'
We copy you down, Eagle.
```
