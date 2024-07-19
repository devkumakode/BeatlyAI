		net = torch.load(f, map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
	return net


def load_json(filename):
	with open(filename) as f:
