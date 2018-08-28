# coding: utf-8
# 设损失函数loss = (w + 1)^2 , 令 w 是常数 5。反向传播就是求最小
# loss 对应的 w 值

import tensorflow as tf
# 定义待优化参数 w 初值赋予5
w = tf.Variable(tf.constant(5, dtype=tf.float32))
# 定义损失函数 loss
loss = tf.square(w+1)
# 定义反向传播方法
# 学习率为：0.2
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
# 生成会话，训练40轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    for i in range(40):
        sess.run(train_step)
        W_val = sess.run(w)
        loss_val = sess.run(loss)
        print("After %s steps: w: is %f,  loss: is %f." %(i, W_val, loss_val))