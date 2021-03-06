# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuanQiuChina(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()


class DaoMuBiJi(scrapy.Item):
    book = scrapy.Field()
    bookTitle = scrapy.Field()
    chaptorNum = scrapy.Field()
    chaptorName = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()