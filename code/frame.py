# 爬取网页通用代码框架
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200，则引发异常
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://item.jd.com/2967929.html"
    # url = "http://www.baidu.com"
    print(getHTMLText(url))



