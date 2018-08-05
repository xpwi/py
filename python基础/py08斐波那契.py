#定义函数
def fib(n):     #打印斐波那契数列 result.append()
    a, b = 0, 1
    while a < n :
        print(a, end=' ')
        a, b = b, a+b

#调用函数
n = eval(input('请输入斐波那契数列上界：'))
fib(n)
print('\n---------------')

#默认参数的值只会被请求一次
i = 5
def f(fig = i):
    print('%d' %fig)
i = 6
print('\n注意区别')
f()
f(i)
