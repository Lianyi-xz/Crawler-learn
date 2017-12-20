#爬取大学排行信息
# import requests
# from bs4 import BeautifulSoup
# url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
# top = []
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     ans = BeautifulSoup(r.text,"html.parser")
#     print(ans)
#     ans_1=ans.find_all('tr')
#     for i in range(1,500):
#         Un = []
#         for j in ans_1[i].td:
#             Un.append(j.string)
#         top.append(Un)
# except:
#     print("信息获取失败")
# print(top)

import requests
from bs4 import BeautifulSoup
import bs4
def getHtml(url,hd):
    try:
        r = requests.get(url,headers = hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ##代表排名的td扩大到整行，排名数据不懂如何查出...
            ulist.append([tds[2].string,tds[1].string,tds[3].string])

def printUnivlist(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    #print("{:^10}\t{:^6}\t{:^10}".format("排名","大学名称","总分"))
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in  range(num):
        u = ulist[i]
        #print("{:^10}\t{:^6}\t{:^10}".format(i+1,u[1],u[2]))
        print(tplt.format(i + 1, u[1], u[2],chr(12288)))

if __name__ == "__main__":
    uinfo = []
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
    hd = {'user-agent': 'Mozilla/5.0'}
    html = getHtml(url,hd)
    fillUnivList(uinfo,html)
    printUnivlist(uinfo,20)