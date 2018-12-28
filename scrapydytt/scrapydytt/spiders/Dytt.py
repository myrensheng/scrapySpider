# -*- coding: utf-8 -*-
import scrapy


class DyttSpider(scrapy.Spider):
    name = 'Dytt'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/']

    def parse(self, response):
        pass
