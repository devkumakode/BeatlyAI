model.add(Dense(1))
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print("ok")
model.fit(X_train, y_train, batch_size=batch_size,
          nb_epoch=nb_epoch, validation_data=(X_test, y_test))