x = tf.placeholder(tf.float32, shape=[None, nr_inputs], name="X_input")
y = tf.placeholder(tf.float32, shape=[None, nr_classes], name="Y_classes")
keep_prob = tf.placeholder(tf.float32)

check_processed_dir_existance()


class CNN(object):
    weights = {
        # 10x1 conv filter, 1 input, 64 outputs
        'wconv1': tf.Variable(tf.random_normal([10, 1, 64])),
        # 10x64 conv filter, 64 inputs, 128 outputs
        'wconv2': tf.Variable(tf.random_normal([10, 64, 128])),
        # 10x128 conv filter, 128 inputs, 128 outputs
        'wconv3': tf.Variable(tf.random_normal([10, 128, 128])),
        # 10x128 conv filter, 128 inputs, 256 outputs
