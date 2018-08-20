# 两个张量的加法
import  tensorflow as tf

# x 是一个一行两列的张量
x = tf.constant([[1.0, 2.0]])
# x 是一个两行一列的张量
w = tf.constant([[3.0], [4.0]])

'''
构建计算图，但不运算
y = XW
 = x1*w1 + x2*w2
'''
# 矩阵相乘
y = tf.matmul(x, w)
print(y)

# 会话：执行节点运算
with tf.Session() as sess:
    print(sess.run(y))