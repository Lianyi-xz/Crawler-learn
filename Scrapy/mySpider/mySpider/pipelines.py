# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyspiderPipeline(object):
    #管道执行前执行方法
    #def __init__(self):
    def open_spider(self,spider):
        self.f = open('itcast_pipline.json','w')
    #管道执行后执行方法
    def close_spider(self,spider):
        self.f.close()
    #管道执行方法
    def process_item(self, item, spider):
        try:
            content = json.dumps(dict(item),ensure_ascii = False) + "\n"
            #self.f.write(content)
            self.f.write(content.encoding('utf-8'))
        except:
            pass
        return item
