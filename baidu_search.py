import requests
def getHtml(url,kv):
    try:
        r = requests.get(url,timeout=30,params=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.request.url,r.status_code,len(r.text)
    except:
        return "产生异常"

if __name__ == "__main__":
    url="http://www.baidu.com/s"
    kv = {'wd':'python'}
    print(getHtml(url,kv))