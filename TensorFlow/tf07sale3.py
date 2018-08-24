# coding:utf-8
'''
- 预测酸奶日销量y，x1和x2是两个影响日销量的因素
  - 应提前采集的数据有：一段时间内，每日的x1因素、x2因素和销量y_。且数据尽量多
  - 在本例子中用销量预测产量，最优的产量应该等于销量，由于目前没有数据集，所以拟造了一套数据集。利用Tensorflow中函数随机生成x1、x2，制造标准答案y_ = x1 + x2，为了真实，求和后还加了正负0.05的随机噪声
  - 我们把这套自制的数据集喂入神经网络，构建一个一层的神经网络，拟合预测酸奶日销量的函数
  -
'''
# 第二种情况：酸奶成本9元，酸奶利润1元
# 预测多了损失大，故不要预测多，故生成的模型会少预测一些
# 导入模块，生成数据集
import tensorflow as tf
import numpy as np

# 一次喂入神经网络8组数据，数值不可以过大
BATCH_SIZE = 8
SEED = 23455
COST = 9
PROFIT = 1

# 基于seed产生随机数
rdm = np.random.RandomState(SEED)
# 随机数返回32行2列的矩阵 表示32组 体积和重量 作为输入数据集
X = rdm.rand(32, 2)
Y_ = [[x1+x2+(rdm.rand()/10.0-0.05)] for (x1, x2) in X]

# 定义神经网络的输入，参数和输出，定义前向传播过程
x = tf.placeholder(tf.float32, shape=(None, 2))
y_ = tf.placeholder(tf.float32, shape=(None, 1))

# w1为2行1列
w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
y = tf.matmul(x, w1)

# 定义损失函数及反向传播方法
# 重新定义损失函数使得预测多了的损失大，于是模型应该偏向少的方向预测
loss = tf.reduce_sum(tf.where(tf.greater(y, y_), COST*(y-y_), PROFIT*(y_-y)))
train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
# 其他优化方法
# train_step = tf.train.GMomentumOptimizer(0.001, 0.9).minimize(loss)
# train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 生成会话，训练STEPS轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    # 训练模型20000轮
    STEPS = 20000
    for i in range(STEPS):
        start = (i*BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y_[start:end]})
        # 没500轮打印一次loss值
        if i % 1000 == 0:
            total_loss = sess.run(loss, feed_dict={x: X, y_: Y_})
            print("After %d training step(s), loss on all data is %g" %(i, total_loss))
            print(sess.run(w1),"\n")

    print("Final w1 is: \n", sess.run(w1))