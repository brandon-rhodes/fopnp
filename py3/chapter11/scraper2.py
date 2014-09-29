
from urllib.parse import urljoin
from ghost import Ghost
from lxml import etree
from scraper1 import main

class GhostVisitor:
    def __init__(self):
        self.ghost = Ghost()

    def GET(self, url):
        page, extra_resources = self.ghost.open(url)
        if page.http_status != 200:
            print('Status', page.http_status, 'for', url)
            return

        html = etree.HTML(self.ghost.content)
        links = html.findall('.//a[@href]')
        for link in links:
            yield self.GET, urljoin(url, link.attrib['href'])

        

if __name__ == '__main__':
    main(GhostVisitor().GET)
