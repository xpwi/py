# 正则结果match的使用案例
import re

# 以下正则分成2个组，以小括号为单位
# [a-z]表示出现小写a-z任意字母都可以，+表示至少出现1次
# 两组之间有一个空格，表示匹配的两个英文字符之间有空格
s = r"([a-z]+) ([a-z]+)"

# 编译
pattern = re.compile(s, re.I)  # s, I表示忽略大小写

m = pattern.match("Hello world wide web")

# group(0) 表示返回整个匹配成功的字符串，即所有小组
s = m.group(0)
print("所有小组的匹配结果：\n", s)

# 返回匹配成功的整个字符串的跨度，即所有小组
a = m.span(0)
print("所有小组的匹配结果跨度：\n", a)

# group(0) 表示返回的第一个分组匹配成功的字符串
s = m.group(1)
print("第1小组的匹配结果：\n", s)

# 返回匹配成功的整个字符串的跨度
a = m.span(1)
print("第1小组的匹配结果跨度：\n", s)

# groups() 打印出所有的小组，等价于m.group(1), m.group(2)...
s = m.groups()
print(s)