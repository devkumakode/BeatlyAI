        'wconv4': tf.Variable(tf.random_normal([10, 128, 256])),
        # fully connected, 1024 outputs
        'wdense1': tf.Variable(tf.random_normal([5376, 1024])),
        # fully connected, 1024 inputs, 2048 outputs
        'wdense2': tf.Variable(tf.random_normal([1024, 2048])),
        # 2048 inputs, class prediction
        'wout': tf.Variable(tf.random_normal([2048, nr_classes]))
    }

    biases = {
