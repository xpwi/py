from urllib import request

# 使用urllib.request请求一个网页的内容，并把内容打印出来

if __name__ == '__main__':

    # 定义需要爬的页面
    url = "https://jobs.zhaopin.com/CC375882789J00033399409.htm"
    # 打开相应url并把页面作为返回
    rsp = request.urlopen(url)
    # 按住Ctrl键不送，同时点击urlopen，可以查看文档，有函数的具体参数和使用方法

    # 把返回结果读取出来
    html = rsp.read()

    print(html)
