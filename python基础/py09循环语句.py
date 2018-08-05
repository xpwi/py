n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

#无限循环
var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字(输入0退出)："))
    if num == 0:
        break
    else:
        print("你输入的数字是: ", num)

print("Good bye!")