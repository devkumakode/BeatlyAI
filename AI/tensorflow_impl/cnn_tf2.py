         x = Conv1D(256, 10, activation='relu')(x)
         x = MaxPool1D()(x)
         x = BatchNormalization()(x)

         x = Flatten()(x)
         x = Dense(1024, activation='relu', name='dense_1')(x)
