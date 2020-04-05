# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs


class JobscpiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('51job.csv', 'w', encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['name', 'corp', 'city', 'salary', 'pub_date'])

    def process_item(self, item, spider):
        # 在Spider模块使用yield提交一个item对象，会触发process_item方法
        self.wr.writerow([item['name'], item['corp'], item['city'], item['salary'], item['pub_date']])
        return item

    def close_spider(self, spider):
        self.file.close()
