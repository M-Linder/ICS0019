import scrapy
"""
@author: matlin
scrapy runspider -O .\output\scrapy.json ScrapySpider.py
"""


class ScrapySpider(scrapy.Spider):
    name = "onoff_spider"
    url = "https://anix-shop.com/product-category/figuurid-ja-manguasjad/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
    }

    def start_requests(self):
        yield scrapy.http.Request(self.url, headers=self.headers)

    def parse(self, response):

        ITEM_SELECTOR = '.product'

        for brickset in response.css(ITEM_SELECTOR):
            NAME_SELECTOR = 'h2 ::text'
            DISCOUNTED_PRICE = '.price ins bdi ::text'
            MAIN_PRICE = '.price bdi ::text'
            PICTURE_HREF = 'img::attr(data-src)'

            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'price':
                    brickset.css(DISCOUNTED_PRICE)[-1].extract() if not brickset.css(MAIN_PRICE)[-1].extract()
                    else brickset.css(MAIN_PRICE)[-1].extract(),
                'picture': brickset.css(PICTURE_HREF).extract_first(),
            }

        NEXT_PAGE_SELECTOR = 'a.next ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse, headers=self.headers)
