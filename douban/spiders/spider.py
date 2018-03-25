# -*- coding: utf-8 -*-
import scrapy
from ..items import HuanQiuChina


class Douban(scrapy.Spider):
    name = 'huanqiu_china'
    start_urls = ['http://china.huanqiu.com/']

    def parse(self, response):
        media_xpath = '/html/body/div[4]/div[1]/div[7]/div[1]/ul/li/a'
        title_xpath = './dl/dt/h3/text()'
        content_xpath = './@href'
        medias = response.xpath(media_xpath)
        for media in medias:
            try:
                title = media.xpath(title_xpath).extract()[0]
                content = media.xpath(content_xpath).extract()[0]
                item = HuanQiuChina()
                item['title'] = title
                item['content'] = content
                print(item)
                yield item
            except:
                continue


