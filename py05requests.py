# 百度翻译
import requests
import json

def fanyi(keyword):
    url = 'http://fanyi.baidu.com/sug'

    # 定义请求参数
    data = {
        'kw': keyword
    }

    # 发送请求，抓取信息
    res = requests.post(url,data=data)

    # 解析结果并输出
    str_json = res.text

    myjson = json.loads(str_json)
    info = myjson['data'][0]['v']
    print(info)

if __name__=='__main__':
    while True:
        keyword = input('请输入翻译的单词：')
        if keyword == 'q':
            break
        fanyi(keyword)
