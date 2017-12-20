#下载图片
#URL 文件之间使用"//"符号 非"\"符号

import requests
import os
url = "http://pic4.nipic.com/20091217/3885730_124701000519_2.jpg"
root = "C://Users//user//Desktop//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取异常")

