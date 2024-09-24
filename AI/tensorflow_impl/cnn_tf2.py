         x = BatchNormalization()(x)
         x = Dropout(dropout)(x)

         x = Dense(2048, activation='relu', name='dense_2')(x)
         x = BatchNormalization()(x)
