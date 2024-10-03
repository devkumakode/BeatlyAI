        return out


class HeartNet(nn.Module):
    def __init__(
        self,
        layers=(1, 2, 2, 2, 2, 2, 2, 2, 1),
        num_classes=1000,
        zero_init_residual=False,
        groups=1,
        width_per_group=64,
        replace_stride_with_dilation=None,
        norm_layer=None,
        block=BasicBlockHeartNet,
