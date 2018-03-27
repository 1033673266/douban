# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class HuanQiuChinaPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient()
        self.db = connection.huan_qiu
        self.tb = self.db.china

    def process_item(self, item, spider):
        self.tb.insert(dict(item))
        return item

    # def process_item(self, item, spider):
    #     with open('test.txt', 'a') as f:
    #         f.write(item['title']+'\n')


class DaoMuBiJiPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient()
        self.db = connection.xiaoshuo
        self.tb = self.db.daomubiji

    def process_item(self, item, spider):
        self.tb.insert(dict(item))
        return item