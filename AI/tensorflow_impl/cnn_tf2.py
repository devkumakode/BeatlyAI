    model.cnn_model.fit(X_train, Y_train, batch_size=batch_size,
                        epochs=epochs, validation_data=(X_val, Y_val),
                        callbacks=model.callbacks)
