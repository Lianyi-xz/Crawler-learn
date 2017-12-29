# -*- coding: utf-8 -*-
import scrapy
#from ITcast.items import ITcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

 #       items = []
        for node in node_list:
            item = {}
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            #返回提取到的每个item数据，给管道文件
            yield item

            #items.append(item)
        #yield items