#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter11/rscrape1.py
# Recursive scraper built using the Requests library.

import argparse, requests
from urllib.parse import urljoin, urlsplit
from lxml import etree

def GET(url):
    text = requests.get(url).text
    html = etree.HTML(text)
    links = html.findall('.//a[@href]')
    for link in links:
        yield GET, urljoin(url, link.attrib['href'])

def scrape(start, url_filter):
    calls_to_make = [start]
    calls_already_made = set()
    while calls_to_make:
        call_info = calls_to_make.pop()
        function, url, *etc = call_info
        print(function.__name__, url, *etc)
        more_calls_to_make = function(url, *etc)
        calls_already_made.add(call_info)
        for call_info in more_calls_to_make:
            if call_info in calls_already_made:
                continue
            function, url, *etc = call_info
            if not url_filter(url):
                continue
            calls_to_make.append(call_info)

def main(GET):
    parser = argparse.ArgumentParser(description='Scrape a simple site.')
    parser.add_argument('url', help='the URL at which to begin')
    start_url = parser.parse_args().url
    starting_netloc = urlsplit(start_url).netloc
    url_filter = (lambda url: urlsplit(url).netloc == starting_netloc)
    scrape((GET, start_url), url_filter)

if __name__ == '__main__':
    main(GET)
