a,b=0,1
while b<1000:
    print(b,end=', ')
    a,b=b,a+b
print('\n---------------')
x=eval(input("请输入x："))
if x<0:
    print('%d为负数' %x)
elif x==0:
    print('x为0')
else :
    print('%d为正数' %x)
print('---------------')

#for循环i从in后面的范围，range(m)即从0开始，生成m个数
for i in range(x):
    print(i)
#break 和 continue和c语言用法一样
