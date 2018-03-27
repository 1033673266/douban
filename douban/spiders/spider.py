# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from douban.items import HuanQiuChina, DaoMuBiJi


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


class DaoMuBiJiSpider(scrapy.Spider):
    name = 'daomubiji'
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-%s' % num for num in range(1, 8)]

    def parse(self, response):
        selector = Selector(response)
        book = selector.xpath('/html/body/div[1]/div/h1/text()').extract()[0]
        chaptors = selector.xpath('/html/body/section/div[2]/div/article/a')
        for chaptor in chaptors:
            chaptor.xpath('./text()').extract()[0].split(' ')
            bookTitle, chaptorNum, chaptorName = chaptor.xpath('./text()').extract()[0].split(' ')
            url = chaptor.xpath('./@href').extract()[0]
            item = DaoMuBiJi()
            item['book'] = book
            item['bookTitle'] = bookTitle
            item['chaptorNum'] = chaptorNum
            item['chaptorName'] = chaptorName
            item['url'] = url
            yield Request(url, callback=self.parseContent, meta={'item': item})

    def parseContent(self, response):
        selector = Selector(response)
        item = response.meta['item']
        html = selector.xpath('/html/body/section/div[1]/div/article').extract()[0]
        item['content'] = html

        yield item
