        w_ori (float tensor): the 3-dim pretrained weight tensor of a convolutional layer.
        ind_layer (int): the index of this layer in the network.
        structure (string): the structure used for grouping the weights in this layer, optional values: 'kernelwise', 'pixelwise', 'channelwise'.
        max_bit (int): the maximum bitwidth used in initialization.
    """
    def __init__(self, w_ori, ind_layer, structure, max_bit):
