# 破解有道词典
# http://fanyi.youdao.com
from urllib import request, parse

def youdao(key):
    
    # url从http://fanyi.youdao.com输入词汇右键检查得到
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=true"
    
    # data从右键检查FormData得到
    data = {
        "i": "girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1523100789519",
        "sign": "b8a55a436686cd8973fa46514ccedbe",
        "doctype": "json",
        "version": "2.1",
        "keyform": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"

    }
    # 对data进行编码，因为参数data需要bytes格式
    data = parse.urlencode(data).encode()
    # headers从右键检查Request Headers得到
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "200",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=685021846@10.168.8.76; JSESSIONID=aaa6qPrsk8RnDf5EahNvw; OUTFOX_SEARCH_USER_ID_NCOO=366356259.5731474; JSESSIONID=abcTY3ZiID37oa9XJhNvw; _ntes_nnid=1f61e8bddac5e72660c6d06445559ffb,1535033370622; ___rl__test__cookies=1535033426167",
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