#bs4 遍历方法
# 上行遍历
#     .parent           父节点标签
#     .parents          节点先辈标签的迭代类型
# 下行遍历
#     .contents         子节点列表
#     .children         子节点的迭代类型
#     .deseendants      子孙节点的迭代类型
# 平行遍历(同一个父节点)
#     .next_sibling       下一个平行节点
#     .previous_sibling   上一个平行节点
#     .next_siblings      所有后续平行节点
#     .previous_siblings  所有前续平行节点

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
