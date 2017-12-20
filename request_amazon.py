import requests
def getHtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url="https://www.amazon.cn/dp/B00S4OK1ZS"
    print(getHtml(url))
