                                                             labels=y)
        return tf.reduce_mean(softmax)

    def optimizer(self, cost):
        adam = tf.train.AdamOptimizer(learning_rate=learning_rate)
        return adam.minimize(cost)

    def evl(self, pred):
        correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
        return tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    def get_data(self):
        return (self.X_train, self.X_test,
                self.Y_train, self.Y_test)


# Construct model
model = CNN()
pred = model.train(x)
