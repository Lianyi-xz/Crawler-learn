# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BiadustocksPipeline(object):
    def process_item(self, item, spider):
        return item

class BiadustocksInfoPipeline(object):
    #管道执行前执行方法
    def open_spider(self,spider):
        self.f = open('BaiduStockInfo.txt','w')
    #管道执行后执行方法
    def close_spider(self,spider):
        self.f.close()

    def process_item(self,item,spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass
        return item

