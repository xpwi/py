# python爬虫实现百度翻译
# urllib和request POST参数提交

from urllib import request,parse
import json

def fanyi(keyword):
    base_url = 'http://fanyi.baidu.com/sug'

    # 构建请求对象
    data = {
        'kw': keyword
    }
    data = parse.urlencode(data)

    # 模拟浏览器
    header = {"User-Agent": "mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}

    req = request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=header)
    res = request.urlopen(req)

    # 获取响应的json字符串
    str_json = res.read().decode('utf-8')
    # 把json转换成字典
    myjson = json.loads(str_json)
    info = myjson['data'][0]['v']
    print(info)

if __name__=='__main__':
    while True:
        keyword = input('请输入翻译的单词：')
        if keyword == 'q':
            break
        fanyi(keyword)

