        fc1 = tf.contrib.layers.batch_norm(fc1, is_training=is_training)
        fc1 = tf.nn.relu(fc1)
        fc1 = tf.nn.dropout(fc1, dropout)

        # Fully connected layer 2
        fc2 = tf.add(tf.matmul(fc1, self.weights['wdense2']), self.biases['bdense2'])
        fc2 = tf.contrib.layers.batch_norm(fc2, is_training=is_training)
        fc2 = tf.nn.relu(fc2)
        fc2 = tf.nn.dropout(fc2, dropout)

        # Output, class prediction
        out = tf.add(tf.matmul(fc2, self.weights['wout']), self.biases['bout'])
        return out

    def conv1d(self, x, W, b, strides=1):
        # conv1d needs a 3-D input([batch, in_width, in_channels]) and
        # filter tensors([filter_width, in_channels, out_channels])
        x = tf.nn.conv1d(x, W, stride=strides, padding='SAME')
        x = tf.nn.bias_add(x, b)
