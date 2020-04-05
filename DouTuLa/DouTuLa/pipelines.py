# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# class DoutulaPipeline(object):
#     def process_item(self, item, spider):
#         return item
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


class DoutulaImagesPipeline(ImagesPipeline):
    # 获取settings中IMAGES_STORE的值
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
    print('IMAGES_STORE:', IMAGES_STORE)

    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        print('item_complted:', results)
        if results[0][0] == True:
            spath = self.IMAGES_STORE + '/' + results[0][1]['path']
            print('spath:', spath)
            dpath = self.IMAGES_STORE + '/' + item['title']
            print('dpath:', dpath)
            os.rename(spath, dpath)
        return item
