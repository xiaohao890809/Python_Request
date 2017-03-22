import requests
import os

# 图片来源的url
url = "http://image.nationalgeographic.com.cn/2017/0310/20170310051823924.jpg"

# 保存文件的目录
root = "..//pic//"

# 截取图片的末尾名字
path = root + url.split('/')[-1]

try:
    # 如果路径不存在，则新建路径
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")

except:
    print("爬取图片失败")