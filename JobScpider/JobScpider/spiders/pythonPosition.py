# -*- coding: utf-8 -*-
import scrapy
from JobScpider.items import JobscpiderItem


class PythonpositionSpider(scrapy.Spider):  # scrapy.Spider:基本的爬虫类
    name = 'pythonPosition'  # 爬虫名称 ，唯一
    allowed_domains = ['51job.com']  # 能够爬取的域名
    start_urls = [
        'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']  # 起始入口地址

    def __init__(self):
        self.city = 10000
        self.max_cities = 40000
        self.page = 1
        self.max_pages = 3
        self.str_url = 'https://search.51job.com/list/0{},000000,0000,00,9,99,python,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    def get_url(self):
        return self.str_url.format(str(self.city), str(self.page))

    def parse(self, response):
        print('parse...')
        # print(response.body)  # body:获取页面内容，bytes格式
        # 招聘条目列表
        ls = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        print('len:', len(ls))
        for each in ls:
            # 招聘职位
            name = each.xpath('./p/span/a/text()').extract()[0].strip()
            self.log('name:' + name)
            # 招聘公司
            corp = each.xpath('.//span[@class="t2"]/a/text()').extract()[0].strip()
            self.log('corp:' + corp)
            # 工作地点
            city = each.xpath('.//span[@class="t3"]/text()').extract()[0].strip()
            self.log('city:' + city)
            # 发布的时间
            pub_date = each.xpath('.//span[@class="t5"]/text()').extract()[0].strip()
            self.log('pub_date:' + pub_date)
            # 薪资待遇
            salary = each.xpath('.//span[@class="t4"]/text()').extract()
            if len(salary) > 0:
                salary = salary[0]
            else:
                salary = '面议'
            self.log('salary:' + salary)
            self.log('=' * 100)
            item = JobscpiderItem()  # 生成item对象
            item['name'] = name
            item['corp'] = corp
            item['city'] = city
            item['salary'] = salary
            item['pub_date'] = pub_date
            # yield: 把封装的数据提交给pipeline
            yield item

        # 翻页处理
        self.page += 1
        if self.page <= self.max_pages:
            url = self.get_url()
            print('page:', self.page, 'url:', url)
            # yield:把请求对象发送到请求等待队列
            req = scrapy.Request(url, callback=self.parse)
            yield req
        else:
            # 换城市
            self.city = self.city + 10000
            if self.city <= self.max_cities:
                self.page = 1
                print('page:', self.page, 'city:', self.city)
                # 封装请求对象
                url = self.get_url()
                req = scrapy.Request(url, callback=self.parse)
                # 把请求对象发送到请求等待队列
                yield req
