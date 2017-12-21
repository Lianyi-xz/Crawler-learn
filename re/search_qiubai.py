#糗百段子爬虫
import requests
import re
from bs4 import BeautifulSoup

#获取8小时内段子总页数
def getPage(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        soup = BeautifulSoup(html,"html.parser")
        return soup.find_all('span',class_='page-numbers')[-1].string
    except:
        return ""

#获取糗百页面
def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


#对糗百网页进行分析
def parserHtml(ilt,html):
    data = {}
    soup = BeautifulSoup(html,"html.parser")
    qiushi = soup.find_all('div',attrs={"class":"article"})
    for i in range(len(qiushi)):
        print(qiushi[i].h2.string)
        auth = re.search(r'/users/\d{8}/',str(qiushi[i]))
        print(auth)
        print(qiushi[i].find('a',attrs={"rel":"nofollow"}).attrs["href"])
        print(qiushi[i].find('a',class_="contentHerf").attrs["href"])
        print(qiushi[i].span)

#输出糗百段子
def printData(ilt):
    pass

if __name__ == '__main__':
   url="https://www.qiushibaike.com"
   page = getPage(url)
   ilt = []
   for i in range(int(page)):
       hr_url="https://www.qiushibaike.com/8hr/page/" + str(i+1)+"/"
       html = getHtml(hr_url)
       parserHtml(ilt,html)
   pass