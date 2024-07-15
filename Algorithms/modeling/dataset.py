
		if type == 'stad':
			scaler = StandardScaler()
			scaler.fit(reshaped_x)
		elif type == 'norm':
