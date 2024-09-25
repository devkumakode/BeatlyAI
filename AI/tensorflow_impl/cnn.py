        conv1 = self.maxpool1d(conv1)
        # Batch Norm Layer 1
        conv1 = tf.contrib.layers.batch_norm(conv1, is_training=is_training)

        # Convolution Layer 2
        conv2 = self.conv1d(conv1, self.weights['wconv2'], self.biases['bconv2'])
        conv2 = self.maxpool1d(conv2)
        # Batch Norm Layer 2
        conv2 = tf.contrib.layers.batch_norm(conv2, is_training=is_training)

        # Convolution Layer 3
        conv3 = self.conv1d(conv2, self.weights['wconv3'], self.biases['bconv3'])
