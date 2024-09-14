
        self.split_data(concat_dataset, validation_size)

        # Reshape input so that we can feed it to the conv layer
        self.X_train = tf.reshape(self.X_train, shape=[-1, n_inputs, 1])
