import tensorflow as tf

w = tf.constant(2.0)
x = tf.placeholder(tf.float32)
b = tf.ones(1)

y = tf.add(tf.math.multiply(w,x), b)

sess = tf.Session()

print(sess.run(y, feed_dict={x:3}))