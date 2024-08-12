        return K.concatenate([x, y], axis=2)

    def zeropad_output_shape(input_shape):
        shape = list(input_shape)
        assert len(shape) == 3
        shape[2] *= 2
        return tuple(shape)

    shortcut = MaxPooling1D(pool_size=subsample_length)(layer)
    zero_pad = (block_index % params["conv_increase_channels_at"]) == 0 \
        and block_index > 0
    if zero_pad is True:
        shortcut = Lambda(zeropad, output_shape=zeropad_output_shape)(shortcut)
