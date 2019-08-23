# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from lianjia_beijing.items import zuFangItem
from lianjia_beijing.items import LianjiaBeijingItem
from lianjia_beijing.items import chengJiaoItem

class LianjiaBeijingPipeline(object):
    collection1 = 'bj_zufang'
    collection2 = 'bj_ershoufang'  #数据库collection名称
    collection3 = 'bj_chengjiao'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print("processing item...")
        if isinstance(item, LianjiaBeijingItem):

            table = self.db[self.collection2]
        elif  isinstance(item, zuFangItem) :
            table = self.db[self.collection1]
        else:
            table = self.db[self.collection3]
        data = dict(item)
        table.insert_one(data)
        return item
