# BeautifulSoup 的使用案例
# 遍历文档对象

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com/'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs 自动解码
content = soup.prettify()

print("=="*12)
# 使用 contents
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)
print("=="*12)