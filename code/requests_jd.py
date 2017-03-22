from PythonRequests.frame import getHTMLText

# 用http是可以的，但是用https就报错了
url = "http://item.jd.com/2967929.html"

jd_text = getHTMLText(url)

print (jd_text[:1000])