# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import redis
from scrapy.exceptions import DropItem

class XcfPipeline(object):
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='spider1807',
            user='root',
            password='liuda6015?',
            charset='utf8',
        )
        self.cur = self.conn.cursor()
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
    def process_item(self, item, spider):
        sql = """
            INSERT INTO xcf(do_num, do_text) VALUES (%s, %s)
        """
        self.cur.execute(sql, (item['do_nums'], item['do']))
        self.conn.commit()
        return item
