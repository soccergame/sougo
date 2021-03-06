import tensorflow as tf
import numpy as np

## Save to file
# remember to define the same dtype and shape when restore
W = tf.Variable([[2,5,7],[11,13,19]], dtype=tf.float32, name='weights')
b = tf.Variable([[23,29,31]], dtype=tf.float32, name='biases')
# initialization
init = tf.global_variables_initializer()
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)
    save_path = saver.save(sess, "folder_for_nn/save_net.ckpt")
    print("Save to path: ", save_path)
