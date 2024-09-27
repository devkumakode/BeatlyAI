        # Reshape conv4 output to fit fully connected layer input
        # shape_size is a cause for errors, it is determined using
        # conv4.shape[1]*conv4.shape[2] and also has to be changed in weight definition
        shape_size = conv4.shape[1] * conv4.shape[2]
        fc1 = tf.reshape(conv4, [-1, shape_size])

        # Fully connected layer 1
        fc1 = tf.add(tf.matmul(fc1, self.weights['wdense1']), self.biases['bdense1'])
