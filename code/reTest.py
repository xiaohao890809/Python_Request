import re

# search的用法
match = re.search(r'[1-9]\d{5}', 'BIT 100008')
if match:
    print(match.group(0))

# match的用法，从头开始匹配的
match = re.match(r'[1-9]\d{5}', '100008 BIT')
if match:
    print(match.group(0))

# 找出所有匹配的结果
print(re.findall(r'[1-9]\d{5}', '100008 BIT 100009 TSH'))

print(re.split(r'[1-9]\d{5}', '100008BIT 100009TSH'))

# 限制maxsplit，只匹配第一个结果
print(re.split(r'[1-9]\d{5}', '100008BIT 100009TSH', maxsplit=1))

# 迭代器，对每一次结果进行处理
for m in re.finditer(r'[1-9]\d{5}', '100008BIT 100009TSH'):
    if m:
        print(m.group(0))

# 用新的字符串替换之前的
print(re.sub(r'[1-9]\d{5}', ':zipcode', '100008BIT 100009TSH'))