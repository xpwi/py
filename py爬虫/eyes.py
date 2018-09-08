# coding:utf-8
'''
使用爬虫提高文章访客说明：
1.本爬虫使用代理IP
2.伪装浏览器
3.粘贴地址即可使用
'''
from urllib import request,error

if __name__ == '__main__':

    # 将需要访问的地址替换下面地址
    url = "https://www.cnblogs.com/xpwi/"

    # 设置代理地址，代理IP一般20天左右会失效
    # 获取最新代理IP，参考文章：https://www.cnblogs.com/xpwi/p/9600727.html
    # 1.日本
    # proxy = {'http': '140.227.65.196:3128'}
    # 2.俄罗斯
    proxy = {'http': '94.242.59.135:1448'}

    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)

    # 下面再进行访问url就会使用代理服务器
    # 更换浏览器型号，参照：https://www.cnblogs.com/xpwi/p/9600719.html
    try:
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163")

        rsp = request.urlopen(req)

        html = rsp.read().decode()
        print("访问成功访客+1，以下是该网页的HTML：\n",html,"\n访问成功访客+1，以上是该网页的HTML\n")

    except error.HTTPError as e:
        print(e)

    except Exception as e:
        print(e)