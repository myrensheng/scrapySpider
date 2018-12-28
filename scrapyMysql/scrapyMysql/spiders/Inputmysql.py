# -*- coding: utf-8 -*-
import scrapy

from scrapyMysql.items import ScrapymysqlItem


class InputmysqlSpider(scrapy.Spider):
    name = 'Inputmysql'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']


    def parse(self, response):
        contents = response.css("div.quote")
        item = ScrapymysqlItem()  # 实例化item类
        for content in contents:
            item["saying"] = content.css('.text::text').extract_first()  # 名言，字符串
            tag = content.css('.tags .tag::text').extract()  # 标签：['木心', '智慧']
            tag = "/".join(tag)
            item["tag"] = tag
            yield item  # 将数据图区交给pipeline处理
        # next_page = response.xpath("//ol[@class='page-navigator']/li/a/@href").extract()
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)

