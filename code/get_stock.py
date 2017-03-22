import os
import traceback

import requests
from bs4 import BeautifulSoup
import re

# 优化代码
def getHTMLText(url, code = 'utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

def getStockList(lst, stockUrl):

    # 1.获取网页信息
    html = getHTMLText(stockUrl, 'GB2312')

    # 2.开始煲汤
    soup = BeautifulSoup(html, 'html.parser')

    # 3.找到所有的a标签
    a = soup.find_all('a')

    # 4.遍历所有的标签，使用正则表达式提取其中的股票信息
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])

        # 遇见异常，跳过继续执行
        except:
            continue

def getStockInfo(lst, stockUrl, fpath):

    count = 0

    # 遍历所有股票列表，拼接新的url
    for stock in lst:
        url = stockUrl + stock + '.html'

        # 获取网页信息
        html = getHTMLText(url)

        try:
            if html == '':
                continue

            # 进行煲汤
            soup = BeautifulSoup(html, 'html.parser')

            # 初始化字典
            stockDic = {}

            # 找出对应的div
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            # 接着找股票的名字
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            stockDic.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valList[i].text
                stockDic[key] = val

            # mac下文件路径的处理，加入扩展名
            path = os.path.expanduser(fpath)

            # 将字典写入文件中
            with open(path, 'a', encoding='utf-8') as f:
                f.write(str(stockDic) + '\n')
                # 打印进度条的速度，\r是为了让每次打印重头开始，end=''是为了不换行
                count += 1
                print('\r当前速度为: {:.2f}%'.format(count*100/len(lst)), end='')

        except:
            count += 1
            print('\r当前速度为: {:.2f}%'.format(count * 100 / len(lst)), end='')
            # traceback.print_exc()
            continue


def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = r'~/Desktop/BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    print(slist)
    getStockInfo(slist, stock_info_url, output_file)

main()