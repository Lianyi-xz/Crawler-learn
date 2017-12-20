#爬取京东商品内容
import requests
def getHtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "产生异常"

if __name__ == "__main__":
    url="https://item.jd.com/5419369.html"
    print(getHtml(url))
