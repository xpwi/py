# 案例v7百度翻译
# 使用Request
from urllib import request,parse
import json

baseurl = 'http://fanyi.baidu.com/sug'
keyword = input("请输入需要翻译的内容：")
data = {
    'kw': keyword
}

# 需要使用parse模块对data进行编码
data = parse.urlencode(data)
data = data.encode('utf-8')

header = {
    'Content-Length':len(data)
}
# 构造Request实例
req = request.Request(url=baseurl,data=data,headers=header)

# 发出请求
rsp = request.urlopen(req)

json_data = rsp.read().decode()

# 把json字符串转换为字典
json_data = json.loads(json_data)

for item in json_data['data']:
    # if item['k'] == keyword:
        print(item['k'], ": ", item['v'])