import requests

# head方法
r = requests.head("http://httpbin.org/get")
print(r.headers) # 这个方法可以快速获取网页的简洁信息
print(r.text) # 打印出来为空

# post方法
payload = {'key1':'value1','key2':'value2'}
r = requests.post("http://httpbin.org/post",data=payload)
# 自动编码为form（表单）
print(r.text)

r = requests.post("http://httpbin.org/post",data='ABC')
# 自动编码为data
print(r.text)


