
from urllib.parse import urljoin
from ghost import Ghost
from lxml import etree
from scraper1 import main

class GhostVisitor:
    def __init__(self):
        self.ghost = Ghost()

    def GET(self, url):
        page, resources = self.ghost.open(url)
        if page.http_status != 200:
            print('Status', page.http_status, 'for', url)
            return

        yield from self.parse(page)

        js = 'document.getElementsByTagName("form").length'
        form_count, resources = self.ghost.evaluate(js)
        if form_count:
            yield self.submit_form, url

    def parse(self, page):
        html = etree.HTML(self.ghost.content)
        links = html.findall('.//a[@href]')
        for link in links:
            yield self.GET, urljoin(page.url, link.attrib['href'])

    def submit_form(self, url):
        page, resources = self.ghost.open(url)
        page, resources = self.ghost.fire_on("form", "submit",
                                             expect_loading=True)
        yield from self.parse(page)

if __name__ == '__main__':
    main(GhostVisitor().GET)
