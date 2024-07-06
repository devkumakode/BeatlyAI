		super().__init__()
		self.batch_size = batch_size
		self.features = nn.Sequential(
			nn.Conv1d(in_channels=input_size, out_channels=1, kernel_size=kernel_size, padding=0),
			nn.ReLU(),
