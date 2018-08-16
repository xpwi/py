# 更改UserAgent，进行伪装
from urllib import  request,error

if __name__ == '__main__':

    url = "http://www.baidu.com/"

    try:

        # 1.使用head方法伪装UA
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163'
        # req = request.Request(url, headers=headers)

        # 2.使用add_header方法
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163")

        rsp = request.urlopen(req)

        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)

    except error.URLError as e:
        print(e)

    except Exception as e:
        print(e)

    print("访问完成！")
