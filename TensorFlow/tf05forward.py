# coding:utf-8
# 前向传播
# 两层简单神经网络（全连接）
import tensorflow as tf

# 定义输入和参数
# x用一行两列的张量表示
x = tf.constant([[0.7, 0.5]])
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 定义前向传播的过程
# 矩阵相乘，不运算
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 用会话计算结果
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    print("y in tf05forward is:\n", sess.run(y))

# 结果：
# [[3.0904665]]