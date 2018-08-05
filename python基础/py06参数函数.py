#含参数函数
def ChangeInt(a):
    a = 10
    print('a为：%d' %a)


b = 2
ChangeInt(b)
print('b为：%d' %b)  # 结果是 2
#意思就是参数传递方式是值传递，不会对原来的值进行修改

#可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]) #添加1,2,3,4
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)
#总结 传可变参数时，调用函数后，原始参数的数值改变