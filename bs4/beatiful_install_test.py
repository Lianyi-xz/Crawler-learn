#测试bs4 是否成功安装
# Tag                标签 < tag > 整个html文件
# Name               标签的名字 < tag >.name
# Attributes         标签属性 < tag >.attrs  数组形式
# NavigableString    标签内容 < tag >.string
# Comment            标签内容注释部分 < tag >.string
import requests
from bs4 import BeautifulSoup
url="http://python123.io/ws/demo.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    demo = r.text
    soup = BeautifulSoup(demo,"html.parser")
    print(soup.prettify())
except:
    print("返回异常")