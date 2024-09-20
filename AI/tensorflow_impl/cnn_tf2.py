
        if verbose:
            print("X_train shape: {}".format(self.X_train.shape))
            print("Y_train shape: {}".format(self.Y_train.shape))
            print("X_test shape: {}".format(self.X_test.shape))
            print("Y_test shape: {}".format(self.Y_test.shape))
            print("X_val shape: {}".format(self.X_val.shape))
            print("Y_val shape: {}".format(self.Y_val.shape))

    def define_model(self):

         inputs = tf.keras.Input(shape=(n_inputs, 1), name='input')

         # 64 filters, 10 kernel size
         x = Conv1D(64, 10, activation='relu')(inputs)
         x = MaxPool1D()(x)
         x = BatchNormalization()(x)
