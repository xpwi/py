# BeautifulSoup 的使用案例

from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com/'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs 自动解码
content = soup.prettify()
print(content)
