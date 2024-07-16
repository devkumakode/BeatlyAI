    return nn.Conv1d(in_planes, out_planes, kernel_size=1, stride=stride, bias=False)


class BasicBlockHeartNet(nn.Module):
    expansion = 1

    def __init__(
