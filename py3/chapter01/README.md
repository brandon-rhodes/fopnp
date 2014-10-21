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

```
$ python search1.py
(41.521954, -84.306691)
```

```
$ python search2.py
{'lat': 41.521954, 'lng': -84.306691}
```

```
$ python search3.py
{'lat': 41.521954, 'lng': -84.306691}
```

```
$ python search4.py
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Date: Tue, 21 Oct 2014 22:23:09 GMT
Expires: Wed, 22 Oct 2014 22:23:09 GMT
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

