import requests
from bs4 import BeautifulSoup
import bs4
import numpy as np

# 从网络上获取大学排名网页内容
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取网页内容失败")
        return ""


# 提取网页内容中信息到合适的数据结构
def fillUnivList(uList, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td') # 是括号
            uList.append([tds[0].string, tds[1].string, tds[3].string])

# 利用数据结构展示并输出结果
def printUnivList(uList, num):
    # 优化中文对齐问题
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "分数", chr(12288)))
    for i in range(num):
        uni = uList[i]
        # #使用空格补齐空位
        print(tplt.format(uni[0], uni[1], uni[2], chr(12288)))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    print(uinfo)
    printUnivList(uinfo,20)

main()