#bs4 基本元素
import requests
from bs4 import BeautifulSoup
url="http://python123.io/ws/demo.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    #对网页内容进行解析
    soup = BeautifulSoup(demo,"html.parser")
    #查看根标签名字
    print(soup.name)
    #查看a标签的父标签名字
    print(soup.a.parent.name)
    #查看a标签属性
    print(soup.a.attrs)
    #查看a标签的class和href属性
    print(soup.a.attrs['class'])
    print((soup.a.attrs['href']))
    print(soup.a.string)
    print(soup.p.string)
except:
    print("返回异常")
