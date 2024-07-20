		data = json.load(f)
		f.close()

		return data


def save_as_pkl(filename_path, data):
	with open(filename_path, 'wb') as f:
		pickle.dump(data, f)
		f.close()


def plotecg(x, y, start, end):
	x = x[start:end, 0]
