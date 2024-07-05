from math import sqrt

import einops
from einops.layers.torch import Reduce
import torch
import torch.nn as nn


class LinearEmbedding(nn.Sequential):

    def __init__(self, input_channels, output_channels) -> None:
        super().__init__(*[
