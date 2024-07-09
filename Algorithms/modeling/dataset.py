class PyTorchMinMaxScalerVectorized(object):

	def __init__(self, fitted_min_max_scaler: MinMaxScaler):
		self.fitted_min_max_scaler: MinMaxScaler = fitted_min_max_scaler

	def __call__(self, tensor):
		return torch.tensor(self.fitted_min_max_scaler.transform(tensor.numpy()))


def fit_min_max_scaler (path, type='stad'):
	with open(path, 'rb') as f:
		x, y = pickle.load(f)

		reshaped_x = x.reshape((x.shape[0] * x.shape[1], x.shape[2]))
