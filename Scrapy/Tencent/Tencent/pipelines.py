# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def open_spider(self,spider):
        self.f = open('tencent_hr.json', 'wb+')

    def process_item(self, item, spider):
        content = json.dumps(item,ensure_ascii=False)+",\n"
        self.f.write(content.encode('utf-8'))

    def close_spider(self, spider):
        self.f.close()
