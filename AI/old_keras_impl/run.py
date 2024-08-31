model = Sequential()
model.add(Convolution1D(nb_filters, 3, input_shape=shape, activation='relu'))
model.add(Dropout(0.25))
model.add(Convolution1D(nb_filters, 3, activation='relu'))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
