# -*-coding: utf-8 -*-
import tensorflow as tf
# numpy 是一个科学计算工具包，这里通过numpy生成模拟数据集
import numpy as np

# 全局参数
# 定义训练batch大小
batch_size = 8
# 定义学习率
learning_rate = 0.001

# 通过随机数生成一个模拟数据集。
rdm = np.random.RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
# 定义规则给出样本的标签。在这里假定所有3 * X1 -2 * X2 >=3为正样本（合格的零件），
# 其他为负样本（不合格的零件）。在这里使用0表示负样本，使用1表示正样本。
Y = [[int(3 * x1 - 2 * x2 >= 0)] for (x1, x2) in X]

def inputs():
    # 定义placeholder作为存放输入数据的地方，
    # 在shape的第一个维度上使用None可以方便使用不同的batch大小
    x = tf.placeholder(dtype=tf.float32, shape=[None, 2], name="input")
    y_ = tf.placeholder(dtype=tf.float32, shape=[None, 1], name="label")
    return x, y_

def inference(x):
    # 声明w1， w2变量，对应于前馈网络中有输入层到隐藏层的权值和从隐藏层到输出层的权值
    # 使用N（0,1）正太分布随机初始化
    w1 = tf.Variable(tf.random_normal(shape=[2, 3], stddev=1.0, seed=0))
    w2 = tf.Variable(tf.random_normal(shape=[3, 1], stddev=1.0, seed=0))
    # 神经网络的前馈过程
    a = tf.matmul(x, w1)
    y = tf.matmul(a, w2)
    return y, w1, w2

def loss(y_pred, y_real):
    # 定义损失函数刻画预测值和真实值的误差
    cross_entropy = -tf.reduce_mean(y_real * tf.log(tf.clip_by_value(y_pred, 1e-10, 1.0)))
    return cross_entropy

def train_optimizer(losses):
    # 定义反向传播优化算法优化神经网络参数
    train_op = tf.train.AdamOptimizer(learning_rate).minimize(losses)
    return  train_op



def main():
    # 定义模型输入
    x, y_ = inputs()
    # 前向传播
    y_pred, w1, w2 = inference(x)
    # 计算loss
    losses = loss(y_pred, y_)
    # 定义训练优化器
    train_op = train_optimizer(losses)
    # 迭代训练
    with tf.Session() as sess:
        # 初始化变量
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        # 训练前的参数
        print(sess.run(w1))
        print(sess.run(w2))
        # 设定训练的轮数
        steps = 5000
        for i in range(steps):
            # 每次选取batch_size个样本训练
            start = (i * batch_size) % dataset_size
            end = min(start + batch_size, dataset_size)

            # 通过选取的样本训练神经网络并更新参数
            sess.run(train_op, feed_dict={x: X[start:end], y_:Y[start:end]})
            if i % 500 == 0:
                # 每隔一段时间计算在所有数据上的交叉熵并输出
                total_cross_entropy = sess.run(
                    losses, feed_dict={x: X, y_: Y})
                print("After %d training steps, cross entropy on all data is %g"
                      % (i, total_cross_entropy))
        # 训练后的参数
        print(sess.run(w1))
        print(sess.run(w2))

if __name__ == "__main__":
    main()