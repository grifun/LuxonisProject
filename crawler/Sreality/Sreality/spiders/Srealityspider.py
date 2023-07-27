import scrapy
from scrapy_playwright.page import PageMethod


class SrealityspiderSpider(scrapy.Spider):
    name = "Srealityspider"
    url = "https://www.sreality.cz/en/search/for-sale/apartments"
    
    def start_requests(self):
        # iterate over pages (given by input parameter) and parse all of them
        try:
            i_start = int(self.from_page)
            i_end = int(self.to_page)
        except:
            i_start = 1
            i_end = 11
        for i in range(i_start, i_end):
            yield scrapy.Request(self.url+"?page="+str(i),
            meta=dict(
                playwright=True,                #enables page interpretation by Javascript
                playwright_include_page=True,   #stores JS output for future parsing
                playwright_page_methods=[       #the parsing waits until this div is produced by JS
                    PageMethod('wait_for_selector', 'div.dir-property-list')
                ]
            ))

    async def parse(self, response):
        for product in response.css('div.property.ng-scope'):
            yield{
                'title': product.css('span.name.ng-binding::text').get(),
                #'title': product.css('div.text-wrap').get(),   #to parse all of the Title text, not just text under tag "Title"
                'image_urls': product.css('img::attr(src)').getall(),
                'check': "1"                                    #just a sanity check for debugging purposes)
            }
