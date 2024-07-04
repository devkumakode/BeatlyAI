					num_layers=num_layers,
					batch_first=True,
					bidirectional=True
			),
		)
		self.classifier = torch.nn.Sequential(
			torch.nn.Linear(2*hidden_size, 2*hidden_size),
			torch.nn.ReLU(inplace=True),
			torch.nn.Dropout(),

			torch.nn.Linear(2 * hidden_size, 2 * hidden_size),
			torch.nn.ReLU(inplace=True),
			torch.nn.Dropout(),
		)
		self.output = torch.nn.Linear(2*hidden_size, out_size)
