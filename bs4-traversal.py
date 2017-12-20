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
    print(soup.head.contents)
    print(len(soup.body.contents))
    print(soup.body.contents[1])
    print(soup.children)
    soup.prettify()
except:
    print("返回异常")
#上行遍历
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
