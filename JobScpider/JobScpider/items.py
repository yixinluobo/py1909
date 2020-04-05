# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 职位名
    city = scrapy.Field()  # 工作地点
    corp = scrapy.Field()  # 公司
    salary = scrapy.Field()  # 薪资
    pub_date = scrapy.Field()  # 发布时间
