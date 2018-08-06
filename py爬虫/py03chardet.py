# py03chardet.py
# 使用request下载页面，并自动检测页面编码

from urllib import request
import chardet

if __name__ == '__main__':

    url = 'https://jobs.zhaopin.com/CC375882789J00033399409.htm'

    rsp = request.urlopen(url)
    # 按住Ctrl键不送，同时点击urlopen，可以查看文档，有函数的具体参数和使用方法

    html = rsp.read()
    cs = chardet.detect(html)

    print("cs的类型：{0}".format(type(cs)))
    print("监测到的cs数据：{0}".format(cs))

    html = html.decode(cs.get("encoding", "utf-8"))
    # 意思是监测到就使用监测到的，监测不到就使用utf-8

    print("HTML页面为：\n%s" % html)
