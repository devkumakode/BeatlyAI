    return Activation('softmax')(layer)

def add_compile(model, **params):
    from keras.optimizers import Adam
