    def maxpool1d(self, x, pool_size=2):
        # [batch, height, width, channels] input type: tf.float32
        return tf.contrib.keras.layers.MaxPool1D(pool_size=pool_size)(x)

    def cost(self, pred):
        softmax = tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred,
