import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(demo, "html.parser")

# 格式化html
print(soup.prettify())

tag = soup.a
print(tag.attrs)
print(tag.attrs['class'])
print(tag.attrs['href'])
print(type(tag.attrs))
print(type(tag))

print(soup.a)
# 打印标签里面的内容
print(soup.a.string)
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))

newSoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>","html.parser")
print(newSoup.b.string)
# 注释的类型是不一样的，但是打印的时候没有打印出来
print(type(newSoup.b.string))
print(newSoup.p.string)
print(type(newSoup.p.string))

print(soup.head)
print(soup.head.contents)

print(soup.body.contents)
print(len(soup.body.contents))
print(soup.body.contents[1])

# 遍历儿子节点
for child in soup.body.children:
    print(child)

print('------------------')
print(soup.title.parent)
print(soup.html.parent)
print(soup.parent)

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)


print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
print(soup.a.previous_sibling.previous_sibling)
print(soup.a.parent)

# 遍历后续节点
for sibling in soup.a.next_siblings:
    print("next_siblings:", sibling)

# 遍历前续节点
for sibling in soup.a.previous_siblings:
    print("previous_siblings:", sibling)

print('---------')

print(soup.a.prettify())

soup = BeautifulSoup("<p>中文</p>","html.parser")
print(soup.p.string)
print(soup.p.prettify())

soup = BeautifulSoup(demo, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

# 显示所有的标签信息
for tag in soup.find_all(True):
    print(tag.name)

# 引入正则表达式
import re

print(soup.find_all(id=re.compile('link1')))

