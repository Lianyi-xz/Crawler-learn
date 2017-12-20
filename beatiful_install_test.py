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