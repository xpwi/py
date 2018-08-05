basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# 集合格式会有去重的功能

# 条件
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 集合元素的添加，删除
basket.add('x')
print(basket)
basket.update({1, 3})
print(basket)
basket.update([1, 4], [5, 6])
print(basket)
basket.remove("apple")
print(basket)