import torch.nn as nn
import torch.nn.functional as F


def conv_block(in_planes, out_planes, stride=1, groups=1, dilation=1):
    return nn.Conv1d(
        in_planes,
        out_planes,
        kernel_size=17,
        stride=stride,
        padding=8,
        groups=groups,
        bias=False,
        dilation=dilation,
    )


def conv_subsumpling(in_planes, out_planes, stride=1):
