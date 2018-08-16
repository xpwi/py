# 使用代理服务器访问猫眼
# https://maoyan.com/
from urllib import request,error

if __name__ == '__main__':

    url = "https://baidu.com/"

    # 1.设置代理地址
    proxy = {'http': '218.60.8.83:3129'}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)

    # 下面再进行访问url就会使用代理服务器
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)

    except Exception as e:
        print(e)