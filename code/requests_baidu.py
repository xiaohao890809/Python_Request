import requests

# 搜索的关键字
kv = {'wd':'Python'}
try:
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.status_code)
    # 搜索的url
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬虫失败")