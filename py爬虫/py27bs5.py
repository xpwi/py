# BeautifulSoup 的使用案例
# css 选择器

from urllib import request
from bs4 import BeautifulSoup


url = 'http://www.baidu.com/'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs 自动解码
content = soup.prettify()

print("=="*12)
titles = soup.select("title")
print(titles[0])

print("=="*12)
meta = soup.select("meta[content='always']")
print(meta[0])