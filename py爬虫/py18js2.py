# 破解js加密，版本2
'''
通过在js文件中查找salt或者sign，可以找到
1.可以找到这个计算salt的公式
r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
2.sign：n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
md5 一共需要四个参数，第一个和第四个都是固定值得字符串，第三个是所谓的salt，
第二个参数是输入的需要翻译的单词
'''
from urllib import request, parse

def getSalt():
    '''
    salt的公式r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
    把它翻译成python代码
    '''
    import time, random

    salt = int(time.time()*1000) + random.randint(0, 10)

    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()

    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()

    return sign

def getSign(key, salt):

    sign = "fanyideskweb" + key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMD5(sign)
    return sign

def youdao(key):
    # url从http://fanyi.youdao.com输入词汇右键检查得到
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=true"

    salt = getSalt()
    # data从右键检查FormData得到
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
        "doctype": "json",
        "version": "2.1",
        "keyform": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"

    }
    print(data)
    # 对data进行编码，因为参数data需要bytes格式
    data = parse.urlencode(data).encode()

    # headers从右键检查Request Headers得到
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=685021846@10.168.8.76; OUTFOX_SEARCH_USER_ID_NCOO=366356259.5731474; _ntes_nnid=1f61e8bddac5e72660c6d06445559ffb,1535033370622; JSESSIONID=aaaVeQTI9KXfqfVBNsXvw; ___rl__test__cookies=1535204044230",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    youdao("girl")