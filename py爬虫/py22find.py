# findall，finditer的基本使用
import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.findall("I am 18 years old, and 185 high")
print(m)

n = pattern.finditer("I am 18 years old, and 185 high")
print(type(n))

# 迭代器使用for循环输出
for i in n:
    # 只输出i会包含无用数据
    print(i.group())