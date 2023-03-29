#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search4.py

# (The Google API originally used in this example now requires API keys,
#  so here's an alternative that calls openstreetmap.org.)

import socket # socket for network communication
import ssl # ssl for secure socket layer for security
from urllib.parse import quote_plus # quote_plus for encoding

request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: Foundations of Python Network Programming example search4.py\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(address):
    # 암호화 되지 않은 소캣 하나 만들기
    unencrypted_sock = socket.socket()

    unencrypted_sock.connect(('nominatim.openstreetmap.org', 443))
    # 암호화 된 소캣 만들기
    sock = ssl.wrap_socket(unencrypted_sock)
    # request_text를 인코딩해서 보내기
    request = request_text.format(quote_plus(address))

    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        #if there is no more data, then break
        if not more:
            break
        raw_reply += more
        print("request :::::: "+request)
    print("raw_reply_decode :::::: "+raw_reply.decode('utf-8'))
    print("raw_reply :::::: ")
    print(raw_reply)

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
    #geocode("Soongsil University")
