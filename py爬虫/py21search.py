# search的基本使用

import re

s = r'\d+'

pattern = re.compile(s)

# 无参数表示从头开始查找，到最后结束
m = pattern.search("one12two34three56")
print(m.group())

# 参数表明搜查的范围，例如：10-40
m = pattern.search("one12two34three56", 10, 40)
print(m.group())