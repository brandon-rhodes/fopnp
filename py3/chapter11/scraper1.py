
import argparse, requests
from urllib.parse import urljoin, urlsplit
from lxml import etree

def visit1(url):
    text = requests.get(url).text
    html = etree.HTML(text)
    links = html.findall('.//a[@href]')
    return [urljoin(url, link.attrib['href']) for link in links]

def scrape1(start, visit, url_filter):
    links_to_visit = [start]
    already_visited = set()
    while links_to_visit:
        url = links_to_visit.pop()
        print('Visiting', url)
        more_urls = visit(url)
        already_visited.add(url)
        new_urls = set(filter(url_filter, more_urls)) - already_visited
        links_to_visit.extend(new_urls)

def main(scrape, visit):
    parser = argparse.ArgumentParser(description='Scrape a simple site.')
    parser.add_argument('url', help='the URL at which to begin')
    start = parser.parse_args().url
    starting_netloc = urlsplit(start).netloc
    url_filter = (lambda url: urlsplit(url).netloc == starting_netloc)
    scrape(start, visit, url_filter)

if __name__ == '__main__':
    main(scrape1, visit1)
