from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/',one_hot=True)

import tensorflow as tf

sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32,[None,784])
w = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

#Softmax Regression
#公式:y = softmax(Wx+b)
y = tf.nn.softmax(tf.matmul(x,w) + b)

#loss function
#Cross-entropy
y_ = tf.placeholder(tf.float32,[None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
tf.global_variables_initializer().run()

for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    train_step.run({x: batch_xs,y_:batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1),tf.arg_max(y_,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

print(accuracy.eval({x:mnist.test.images,y_:mnist.test.labels}))
