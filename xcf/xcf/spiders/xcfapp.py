# -*- coding: utf-8 -*-
import scrapy

from xcf.items import XcfItem


class XcfappSpider(scrapy.Spider):
    name = 'xcfapp'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['http://www.xiachufang.com/explore/']

    def parse(self, response):
        urls = response.xpath("//ul[@class='list']/li/div/a/@href").extract()
        print(urls)
        for url in urls:
            yield response.follow(url, callback=self.detail_parse)
        next = response.xpath("//a[@class='next']/@href").extract_first()
        if next:
            yield response.follow(next, callback=self.parse)

    def detail_parse(self, response):
        steps = response.xpath("//div[@class='steps']/ol/li")
        for i in steps:
            do = i.xpath("./p/text()").extract_first()
            do_nums = i.xpath("./img/@alt").extract_first()
            item = XcfItem()
            item["do_nums"] = do_nums
            item["do"] = do
            yield item