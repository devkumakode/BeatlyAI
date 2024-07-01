import torch
import torch.nn as nn

import config
from util import load_json


class SegModel(torch.nn.Module):
	def __init__(self, input_size, hidden_size, num_layers, out_size):
		super().__init__()
		self.features = torch.nn.Sequential(
			torch.nn.LSTM(
					input_size=input_size,
					hidden_size=hidden_size,
