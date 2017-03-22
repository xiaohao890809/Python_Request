import requests

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    r = requests.get(url)

    # 查看最开始的headers信息
    print(r.request.headers)
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    # 查看修改后的headers的信息
    print(r.request.headers)
    print(r.text[:1000])
except:
    print("爬虫失败")