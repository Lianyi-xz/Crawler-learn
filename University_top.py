# import requests
# from bs4 import BeautifulSoup
# url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
# top = []
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     ans = BeautifulSoup(r.text,"html.parser")
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
def getHtml(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("信息获取失败")
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            print(tds[0])
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    #print(ulist)
def printUnivlist(ulist,num):
    print("Suc" + str(num))

if __name__ == "__main__":
    uinfo = []
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
    html = getHtml(url)
    fillUnivList(uinfo,html)
    printUnivlist(uinfo,20)