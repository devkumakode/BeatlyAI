         x = Dropout(dropout)(x)

         outputs = Dense(n_classes, activation='softmax', name='predictions')(x)

         self.cnn_model = tf.keras.Model(inputs=inputs, outputs=outputs)
         optimizer = tf.keras.optimizers.Adam(lr=learning_rate)
         accuracy = CategoricalAccuracy()
         self.cnn_model.compile(optimizer=optimizer, loss='categorical_crossentropy',
                                metrics=[accuracy])

    def split_data(self, dataset, validation_size):
        """
        Suffle then split training, testing and validation sets
        """

        # In order to use statify in train_test_split we can't use one hot encodings,
        # so we convert to array of labels
        label_data = np.argmax(self.label_data, axis=1)
