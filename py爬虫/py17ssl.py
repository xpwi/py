'''
使用ssl
1.直接访问https://www.12306.cn/mormhweb/会无法访问，报错如下
 ----------------------------------
 您的连接不是私密连接
 攻击者可能会试图从 www.12306.cn 窃取您的信息
 （例如：密码、通讯内容或信用卡信息）
 -----------------------------------
2.不使用https使用http解可以访问
3.因为12306的证书是自己做的，而不是第三方机构
4.所以说http不安全会泄露个人信息
'''
from urllib import request

import ssl

# 利用非认证上下文环境替换认证的上下文环境
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.12306.cn/mormhweb/"
rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)