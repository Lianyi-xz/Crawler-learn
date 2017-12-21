#淘宝商品爬虫
import requests
import re
#获取淘宝页面
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

#对淘宝页面进行分析
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        return ""

#输出商品信息
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in  ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

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
    printGoodsList(infoList)
