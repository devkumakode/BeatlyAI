        conv3 = self.maxpool1d(conv3)
        # Batch Norm Layer 3
        conv3 = tf.contrib.layers.batch_norm(conv3, is_training=is_training)

        # Convolution Layer 4
        conv4 = self.conv1d(conv3, self.weights['wconv4'], self.biases['bconv4'])
        conv4 = self.maxpool1d(conv4)
        # Batch Norm Layer 4
        conv4 = tf.contrib.layers.batch_norm(conv4, is_training=is_training)

        # Fully connected layer
