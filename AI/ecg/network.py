        kernel_initializer=params["conv_init"])(layer)
    return layer


def add_conv_layers(layer, **params):
    for subsample_length in params["conv_subsample_lengths"]:
        layer = add_conv_weight(
                    layer,
                    params["conv_filter_length"],
                    params["conv_num_filters_start"],
                    subsample_length=subsample_length,
                    **params)
        layer = _bn_relu(layer, **params)
    return layer

def resnet_block(
        layer,
        num_filters,
        subsample_length,
        block_index,
