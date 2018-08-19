# 使用filecookiejar
from urllib import request,parse
from http import cookiejar

# 创建cookiejar的实例
filename = "py15renrenCookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
# 常见cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求的管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    # 负责首次登录，输入用户名和密码，用来获取cookie
    url = 'http://www.renren.com/PLogin.do'

    id = input('请输入用户名：')
    pw = input('请输入密码：')

    data = {
        # 参数使用正确的用户名密码
        "email": id,
        "password": pw
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url,data=data.encode('utf-8'))
    # 使用opener发起请求
    rsp = opener.open(req)

    '''
    保存cookie到文件
    两个参数：
        ignore_discard：表示及时cookie将要被丢弃，是否保存下来
        ignore_expires：表示如果该文件中cookie已经过期，是否保存下来
    '''
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == '__main__':

    login()

