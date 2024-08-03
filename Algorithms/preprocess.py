
	return x_data, y_data


def preprocess_baseline_wander_removal (df, window_len):
	x_data = np.empty((1, window_len, 2))
