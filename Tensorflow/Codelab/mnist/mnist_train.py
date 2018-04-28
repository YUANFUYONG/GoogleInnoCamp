# -*-coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
learning_rate = 0.001
TRAINING_STEPS = 10000
BATCH_SIZE = 64
def conv_layer(input, in_channel, out_channel):
    # 定义卷积层
    w = tf.Variable(tf.truncated_normal([5, 5, in_channel, out_channel], stddev=0.1))
    b = tf.Variable(tf.constant(0.1, shape=[out_channel]))
    #strides里面的每一量对应W在x上的移动步长，比如strides = [1, 2, 3, 4]批，每次移动batch的个数是1；每次移动in_height的数目是2；
    # 每次移动in_width的数目是3；每次移动in_channels的数目是4。当然，每次只应该移动一个量。
    # 注意，batch和in_channels一般每次只会移动1。所以一般形式是strides = [1, stride, stride, 1]。
    conv = tf.nn.conv2d(input, w, strides=[1, 1, 1, 1], padding="SAME")
    act = tf.nn.relu(conv + b)
    return act

def fc_layer(input, size_in, size_out):
    # 定义全连接层
    w = tf.Variable(tf.truncated_normal([size_in, size_out], stddev=0.1))
    b = tf.Variable(tf.constant(0.1, shape=[size_out]))
    fc = tf.matmul(input, w) + b
    return fc

def inference(image, keep_prob):
    # conv1
    conv1 = conv_layer(image,1, 32)
    conv1_pool = tf.nn.max_pool(conv1, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
    # conv2
    conv2= conv_layer(conv1_pool, 32, 64)
    conv2_pool = tf.nn.max_pool(conv2, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
    conv_flaten = tf.reshape(conv2_pool, shape=[-1, 7*7*64])
    # fc1
    fc1 = tf.nn.relu(fc_layer(conv_flaten, 7*7*64, 1024))
    fc1 = tf.nn.dropout(fc1, keep_prob=keep_prob)
    return fc_layer(fc1, 1024, 10)

def inputs():
    # 定义输入
    keep_prob = tf.placeholder(tf.float32, name="keep_prob")
    x = tf.placeholder(tf.float32, shape=[None, 784], name="x")
    y = tf.placeholder(tf.float32, shape=[None, 10], name="labels")
    return x, y, keep_prob

def loss(y_pred, y_real):
    # 定义交叉熵误差
    xent = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(
            logits=y_pred, labels=y_real))
    return xent
def train_optimizer(loss, global_step=None):
    # 定义训练优化器
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss, global_step=global_step)
    return train_step

def accuracy(y_pred, y_real):
    # 定义预测准确率
    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y_real, 1))
    acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    return acc

def train(mnist):
    x, y, keep_prob = inputs()
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    global_step = tf.Variable(0, trainable=False)
    logits = inference(x_image, keep_prob=keep_prob)   # 定义模型
    losses = loss(y_pred=logits, y_real=y)
    train_step = train_optimizer(losses, global_step=global_step)
    acc = accuracy(y_pred=logits, y_real=y)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(TRAINING_STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            _, loss_value, step = sess.run([train_step, losses, global_step],
                                           feed_dict={x: xs, y: ys, keep_prob:0.5})
            if i % 200 ==0:
                print("After %d training step(s), loss on training batch is %g."
                      % (step, loss_value))
            if i % 1000 == 0:
                valid_acc = sess.run(acc, feed_dict={x: mnist.validation.images, y: mnist.validation.labels, keep_prob:1.})
                print("After %d training step(s), accuracy on validation is %g." % (step, valid_acc))
        test_acc = sess.run(acc, feed_dict={x:mnist.test.images, y:mnist.test.labels, keep_prob:1.})
        print("After %d training step(s), accuracy on test is %g." % (TRAINING_STEPS, test_acc))
if __name__ == "__main__":
    mnist = input_data.read_data_sets("data/", one_hot=True)
    train(mnist)