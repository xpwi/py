# BeautifulSoup 的使用案例

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com/'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs 自动解码
content = soup.prettify()

# 虽然原文中有多个 meta 但是使用 soup.meta 只会打印出以第一个
print("soup.meta:\n", soup.meta)
print("=="*12)
print("soup.meta.name:\n",soup.meta.name)
print("=="*12)
print("soup.meta.attrs:\n",soup.meta.attrs)
print("=="*12)
print("soup.meta.attrs['content']:\n",soup.meta.attrs['content'])

# 当然我们也可以对获取到的数据进行修改
soup.meta.attrs['content'] = 'hahahahaha'
print("=="*5, "修改后","=="*5)
print("soup.meta.attrs['content']:\n",soup.meta.attrs['content'])
