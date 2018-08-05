print("Hello, Python!")
print("Hello\nworld!")
#print函数单引号，双引号都会解释里面的\n，如果不想解释在引号前面加r
print(r'Hello\nworld!')
print("Hello\nworld!")
str='Xiaopengwei'
print(str[0])
print(str[0:])
print(str[0:-1])
print('---------')
print(str+' 你好！')
print(str,end=' ')
print(str+' 你好！')

#难点，同时有字符和变量的时候，用一对%来输出变量，在引号后面加 空格%参数名
print('同时输出多个变量')
x = 123
y = 456
print(x)
print("{:.2f}".format(x))
#format格式化输出
print('x的值为%d,y的值为%d,str的值为%s' %(x,y,str))

m = set('abracadabra')
#set表示集合，相同元素只出现一次
print('集合m为：%s' %(m))

a = 'adgdg'
b = 'gerh'
n = a+b
print('a+b为：%s' %(n))
print('a+b为：%s' %(a+b))
print(a+b)
