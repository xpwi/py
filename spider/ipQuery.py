# coding:utf-8
# 测爬虫ip工具
from urllib import request,error

if __name__ == '__main__':
    # 该地址可能会失效，如果失效，参照：
    url = "http://2018.ip138.com/ic.asp"
    rsp = request.urlopen(url)
    html = rsp.read().decode('GBK')
    print(html)
