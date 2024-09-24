            print("X_train shape: {}".format(self.X_train.shape))
            print("Y_train shape: {}".format(self.Y_train.shape))
            print("X_test shape: {}".format(self.X_test.shape))
            print("Y_test shape: {}".format(self.Y_test.shape))

    def train(self, x):
        is_training = not freeze
        # Reshape input so that we can feed it to the first conv layer
        x = tf.reshape(x, shape=[-1, nr_inputs, 1])
        
        # Convolution Layer 1
