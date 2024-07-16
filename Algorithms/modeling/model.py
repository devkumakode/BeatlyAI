		)
	elif model_name == 'cnn-seg-net':
		return CnnSegModel(
				input_size=model_params['input_size'],
				hidden_size=model_params['hidden_size'],
