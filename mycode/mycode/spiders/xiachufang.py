# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class XiachufangSpider(scrapy.Spider):
    name = 'xiachufang'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['http://www.xiachufang.com/explore/']

    def parse(self, response):
        print(response.text)
        urls = response.xpath("//ul[@class='list']/li/div/a/@href").extract()
        print(urls)
        # for url in urls:
        #     yield response.follow(url, callback=self.parse_do)
        # yield

    def parse_do(self, response):
        print(response)
        yield {"anme":"sss"}
