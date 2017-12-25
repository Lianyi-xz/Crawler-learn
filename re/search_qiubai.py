#糗百段子爬虫
#糗事内容抓取存在问题，已决定不再修改
import re
import time
import requests
import xlsxwriter
import numpy as np
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
    soup = BeautifulSoup(html,"html.parser")
    qiushi = soup.find_all('div',attrs={"class":"article"})
    for i in range(len(qiushi)):
        data = { }
        #搜索作者姓名
        data['user'] = re.sub(r'\n','',qiushi[i].h2.string)
        #搜索用户链接
        user = re.search(r'/users/\d{3,10}/',str(qiushi[i]))
        #搜索文章链接
        data['content_url'] = "https://www.qiushibaike.com" + qiushi[i].find('a', class_="contentHerf").attrs["href"]
        #搜索内容文字
        content = qiushi[i].find('div',class_="content")
        #搜索有内容图片
        thumb = qiushi[i].find('div',class_="thumb")
        # #保存用户链接，匿名用户保存None
        if user:
            data['user_url'] = "https://www.qiushibaike.com" + user.group(0)
        else:
            data['user_url'] = "None"
        # #保存内容文字
        if content:
            data['content'] = re.sub(r'\n','',str(content.span.string))
        else:
            data['content'] = "None"
        #保存内容图片
        if thumb:
            data['thumb_url'] = "https:" + thumb.a.img.attrs["src"]
        else:
            data['thumb_url'] = "None"
        ilt.append(data)


#输出糗百段子
def printData(ilt):
    for i in range(ilt.__len__()):
        print("用户名：{:s}".format(ilt[i]['user']))
        print("用户主页：{:s}".format(ilt[i]['user_url']))
        print("糗事主页：{:s}".format(ilt[i]['content_url']))
        print("糗事图片：{:s}".format(ilt[i]['thumb_url']))
        print("糗事：{:s}".format(ilt[i]['content']))
        print("")
        print("")

#保存段子到TXT文件
def saveTxtData(ilt,file):
    with open(file,'a', encoding='utf-8') as f:
        f.write(str(ilt))

#保存段子到xls文件
def saveXlsData(ilt,file):
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet("糗百8小时热门")
    for i in range(ilt.__len__()):
        worksheet.write(i,0,ilt[i]['user'])
        worksheet.write(i, 1, ilt[i]['user_url'])
        worksheet.write(i, 2, ilt[i]['content_url'])
        worksheet.write(i, 3, ilt[i]['thumb_url'])
        worksheet.write(i, 4, ilt[i]['content'])
    workbook.close()

if __name__ == '__main__':
    start_time=time.time()
    url="https://www.qiushibaike.com"
    page = getPage(url)
    ilt = []
    output_txt = 'C:/Users/user/Desktop/qiubai.txt'
    output_xls = 'C:/Users/user/Desktop/qiubai.xlsx'
    for i in range(int(page)):
        time.sleep(np.random.rand()*5)
        try:
           hr_url="https://www.qiushibaike.com/8hr/page/" + str(i+1)+"/"
           html = getHtml(hr_url)
           parserHtml(ilt,html)
        except:
           print("")
    printData(ilt)
    #saveTxtData(ilt,output_txt)
    #saveXlsData(ilt,output_xls)
    end_time=time.time()
    print("爬虫运行时间：",end_time-start_time)