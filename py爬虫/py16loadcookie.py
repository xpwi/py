# 读取cookie文件
from urllib import request,parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('py15renrenCookie.txt', ignore_discard=True, ignore_expires=True)

# 常见cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求的管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def getHomePage():
    # 地址是用在浏览器登录后的个人信息页地址
    url = "http://www.renren.com/967487029/profile"

    # 如果已经执行login函数，则opener自动已经包含cookie
    rsp = opener.open(url)
    html = rsp.read().decode()

    with open("py13rsp.html", "w", encoding="utf-8")as f:
        # 将爬取的页面
        print(html)
        f.write(html)

if __name__ == '__main__':

    getHomePage()

