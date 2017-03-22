import time

# 计算爬取100次网页所需的时间
from PythonRequests.frame import getHTMLText

# 开始时间
start_time = time.time()
url = "http://search.bilibili.com/"

for i in range(100):
    text = getHTMLText(url)

# 结束时间
end_time = time.time()

print("共花费了%0.2f秒" %(end_time-start_time))