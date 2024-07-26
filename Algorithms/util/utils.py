

def plot_learning_curve(data, xlabel, ylabel):
	means = list(map(lambda x: np.mean(x, axis=0), data))
	std = list(map(lambda x: np.std(x, axis=0), data))

	std_plus = [
		means[i] + std[i]
		for i in range(len(means))
	]

	std_minus = [
		means[i] - std[i]
		for i in range(len(means))
