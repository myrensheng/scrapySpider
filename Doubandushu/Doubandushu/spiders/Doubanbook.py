# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoubanbookSpider(CrawlSpider):
    name = 'Doubanbook'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']

    rules = (
        Rule(LinkExtractor(allow=r'^https://book.douban.com/subject/\d+/$'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='paginator']"),follow=True)
)


    def parse_item(self, response):
        i = {}
        i["author"] = response.xpath("//div[@id='info'/a[1]/text()").extract_first()[0].replace(" ","").replace(r"\n","")

        return i
