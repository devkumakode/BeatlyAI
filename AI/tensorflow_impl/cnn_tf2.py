
         x = Conv1D(128, 10, activation='relu')(x)
         x = MaxPool1D()(x)
         x = BatchNormalization()(x)

         x = Conv1D(128, 10, activation='relu')(x)
         x = MaxPool1D()(x)
         x = BatchNormalization()(x)

