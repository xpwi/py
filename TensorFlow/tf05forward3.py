# coding:utf-8
# 前向传播
# 两层简单神经网络（全连接）
# 向神经网络喂入n组特征
import tensorflow as tf

# 定义输入和参数
# 用placeholder实现输入自定义（sess.run中喂多组数据）None表示未知
x = tf.placeholder(tf.float32, shape=(None, 2))
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
    # 字典，喂入多组特征
    print("y in tf05forward2 is:\n", sess.run(y, feed_dict={x:[[0.7,0.5],[0.2,0.3],[0.3,0.4],[0.4,0.5]]}))
    print("w1:", sess.run(w1))
    print("w2:", sess.run(w2))