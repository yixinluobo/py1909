# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoutulaItem(scrapy.Item):
    # define the fields for your item here like:
    # 图片标题
    title = scrapy.Field()
    # 照片链接
    image_url = scrapy.Field()
    # 照片本地保存路径
    image_path = scrapy.Field()
