			torch.nn.LSTM(
					input_size=input_size,
					hidden_size=hidden_size,
					num_layers=1,
					batch_first=True,
					bidirectional=True
			)
		)
		self.deconv = nn.ConvTranspose1d(in_channels=2*hidden_size, out_channels=hidden_size, kernel_size=kernel_size, padding=0)
		self.classifier = torch.nn.Sequential(
			torch.nn.Linear(hidden_size, 2 * hidden_size),
			torch.nn.ReLU(inplace=True),
			torch.nn.Dropout(),
		)
		self.output = torch.nn.Linear(2 * hidden_size, out_size)

	def forward(self, x):
		"""
		:param x: shape(batch, seq_len, input_size) -->  (batch_size, features/input_channels, timesteps/signal_length)
