# 爬虫未使用cookie
from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/967487029/profile"

    rsp = request.urlopen(url)

    html = rsp.read().decode()

    with open("py12rsp.html","w",encoding="utf-8")as f:
        # 将爬取的页面
        print(html)
        f.write(html)