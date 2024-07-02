from keras import backend as K

def _bn_relu(layer, dropout=0, **params):
    from keras.layers import BatchNormalization
