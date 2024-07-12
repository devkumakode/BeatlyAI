

def model_factory (model_name):
	model_params = load_json(config.ROOT_DIR + '/model_params.json')[model_name]

	if model_name == 'seg-net':
		return SegModel(
				input_size=model_params['input_size'],
				hidden_size=model_params['hidden_size'],
				num_layers=model_params['num_layers'],
				out_size=model_params['out_size']
