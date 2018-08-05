from urllib import request

if __name__ == '__main__':

    url = "https://jobs.zhaopin.com/CC375882789J00033399409.htm"
    rsp = request.urlopen(url)
    # 按住Ctrl键不送，同时点击urlopen，可以查看文档，有函数的具体参数和使用方法

    html = rsp.read()

    print(type(html))
    # 可以查看html的类型, 可以查出是bytes类型，就需要解码
    html = html.decode()

    print(html)
