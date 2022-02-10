import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlInPagesSpider(CrawlSpider):
    name = 'crawl_in_pages'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rules = (
        # ссылка на саму книгу
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/h3/a"), callback='parse_item', follow=True),
        # для перехода на след.страницу
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath("//div[contains(@class, 'product_main')]/h1/text()").get()
        item['price'] = response.xpath("//div[contains(@class, 'product_main')]/p[@class='price_color']/text()").get()
        item['img'] = response.xpath("//div[contains(@class, 'item')]/img/@src").getall()
        item['description'] = response.xpath("//div[@id='product_description']/../p/text()").get()
        item['upc'] = response.xpath("//th[contains(text(), 'UPC')]/../td/text()").get()
        return item
