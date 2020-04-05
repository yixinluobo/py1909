# -*- coding: utf-8 -*-
import scrapy
# 链接提取器，描述链接特征
from scrapy.linkextractors import LinkExtractor
# CrawlSpider: 自动化爬取类
# Rule:定义规则
from scrapy.spiders import CrawlSpider, Rule

from DouTuLa.items import DoutulaItem


class DoutulaSpider(CrawlSpider):
    name = 'doutula'
    allowed_domains = ['doutula.com']
    start_urls = ['https://www.doutula.com/article/list/?page=1']
    # 翻页链接提取器
    page_link = LinkExtractor(restrict_xpaths=('//a[@rel="next"]',))
    # 内容链接提取器
    content_link = LinkExtractor(restrict_xpaths=('//a[@class="list-group-item random_list"]',))
    # 定义规则
    rules = [
        Rule(page_link, follow=True),
        Rule(content_link, callback='parse_item')
    ]

    def parse_item(self, response):
        item = DoutulaItem()
        img_ls = response.xpath('//div[@class="pic-content"]/div[@class="artile_des"]//img/@src')
        for img in img_ls:
            self.log(img.extract())
            # 图片链接
            image_url = img.extract()
            # 图片名
            title = image_url.split('/')[-1]
            item['title'] = title
            item['image_url'] = image_url
            yield item
