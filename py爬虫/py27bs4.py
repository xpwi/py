# BeautifulSoup 的使用案例
# 搜索文档对象

from urllib import request
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com/'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs 自动解码
content = soup.prettify()

# 使用 find_all
# 使用 name 参数
print("=="*12)
tags = soup.find_all(name='link')
for i in tags:
    print(i)

# 使用正则表达式
print("=="*12)
# 同时使用两个条件
tags = soup.find_all(re.compile('^me'), content='always')
# 这里直接打印 tags 会打印一个列表
for i in tags:
    print(i)

