# 爬虫使用cookie
from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/967487029/profile"

    headers = {
        # Cookie值从登录后的浏览器，拷贝，方法文章上面有介绍
        "Cookie": "anonymid=jkw22rj1lr18nw; depovince=GW; _r01_=1; JSESSIONID=abcUPkh_yMcQi56IB9avw; ick_login=79ce148f-80c5-4a79-ad1e-897e847d7f34; ick=d4c0f36e-a5b8-4063-b781-8a8474c4a289; t=07c15f420c005cec1ff760ee5370cfeb9; societyguester=07c15f420c005cec1ff760ee5370cfeb9; id=967487029; xnsid=bf077aca; XNESSESSIONID=6302ff129554; BAIDU_SSP_lcr=https://www.baidu.com/link?url=4ejhDX-FjIJI0Ma--EY03Dbwea0D_c1HhU7ExMXfUxO&wd=&eqid=c4ff527c00007cb4000000035b74fb58; wp_fold=0; jebe_key=d4adac05-f904-479c-bf00-a4b55d282a51%7C43e5f9c3c001a1d1846f8b82a462cefd%7C1534398658919%7C1; jebecookies=6031f512-d289-4dff-b1d6-aaa7849bd1ff|||||"
    }

    req = request.Request(url=url,headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open("rsp.html","w",encoding="utf-8")as f:
        # 将爬取的页面
        print(html)
        f.write(html)