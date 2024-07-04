		batch, seq_len, nums_fea = x.size()
		features, _ = self.features(x)
		output = self.classifier(features)
		output = self.output(output.view(batch * seq_len, -1))

		return output


class CnnSegModel(nn.Module):
	"""
		attr 'input_size': number of channels in input signal;
			For example for image recognizition there are 3 channels for R,G and B value;
		attr 'kernel_size': size of the convolving kernel;

		Conv1D excepts the input to be of the shape - [batch_size, input_channels, signal_length]
	"""

	def __init__(self, input_size=1, hidden_size=32, kernel_size=3, out_size=5, batch_size=32):
