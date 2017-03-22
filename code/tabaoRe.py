import re
import requests

def getHTEMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(ilt, html):
    try:
        # 价格 127.00 小数点
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        # *?表示最小匹配
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            # 以数组的形式进行封装
            ilt.append([price, title])
    except:
        print("")

def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            # 44的倍数进行分页处理
            url = start_url + '&s=' + str(44*i)
            html = getHTEMLText(url)
            parsePage(infoList, html)
        except:
            continue

    printGoodList(infoList)

main()