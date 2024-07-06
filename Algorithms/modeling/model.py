			# nn.MaxPool1d(3, stride=1),
			nn.Dropout()
		)
		# Classify output, fully connected layers
		self.memory = nn.Sequential(
