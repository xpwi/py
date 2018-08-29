# 中文unicode案例

import re

hello = u'你好，再见陌生人'

# 中文全角逗号一类的不在[u4e00-u9fa5]范围内
pattern = re.compile(r'[\u4e00-\u9fa5]+')

m = pattern.findall(hello)

print(m)