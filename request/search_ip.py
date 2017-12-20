#查询ip地址
#使用www.ip138.com 网站进行IP查询
import requests
def getHtml(url):
    try:
        r = requests.get(url+'202.204.80.112')
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[-500:]
    except:
        return "产生异常"

if __name__ == "__main__":
    url="http://www.ip138.com/ips138.asp?ip="
    print(getHtml(url))
