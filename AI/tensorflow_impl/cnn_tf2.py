
        self.X_train, self.X_val, self.Y_train, self.Y_val = res

        # Convert the array of labels back into one hot encodings to be able to do training
        self.Y_train = tf.keras.utils.to_categorical(self.Y_train)
        self.Y_test = tf.keras.utils.to_categorical(self.Y_test)
        self.Y_val = tf.keras.utils.to_categorical(self.Y_val)

    def get_data(self):
        return (self.X_train, self.X_test, self.X_val,
                self.Y_train, self.Y_test, self.Y_val)


def main():
    # Construct model
    model = CNN()
    X_train, X_test, X_val, Y_train, Y_test, Y_val = model.get_data()

    # Set start time
    total_time = time.time()
