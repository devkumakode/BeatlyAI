
	def __init__(self, data_path, transform=None):
		self.transform = transform
		with open(data_path, 'rb') as f:
			self.x, self.y = pickle.load(f)

	def __len__ (self):
		return len(self.x)

	def __getitem__ (self, idx):
		if torch.is_tensor(idx):
			idx = idx.tolist()

		ecg = torch.from_numpy(self.x[idx]).float()
