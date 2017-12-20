import requests
from bs4 import BeautifulSoup
import re
#获取淘宝页面
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")

#对淘宝页面进行分析
def parsePage(ilt,html):
    pass

#输出商品信息
def printGoodsList(list):
    pass

if __name__ == '__main__':
    goods = "书包"
    depth = 2
    start_url = "https://s.taobao.com/search?q="+goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '@s='+str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            print("")