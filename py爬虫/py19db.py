# 爬取豆瓣电影数据
# 了解ajax的爬取方式
# https://movie.douban.com/

from urllib import request
import json

# url信息：interval_id表示排名段，limit限制20个
url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20"

rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

# 遍历输出每个'k'和'v'的值
for item in data:
      print("排名：", item['rank'], "\n",
            "名称：", item['title'], "\n",
            "类型：", item['types'], "\n",
            "主演：", item['actors'], "\n",
            "分数：", item['score'],"\n-------------",)