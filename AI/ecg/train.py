    model = network.build_network(**params)

    stopping = keras.callbacks.EarlyStopping(patience=8)
