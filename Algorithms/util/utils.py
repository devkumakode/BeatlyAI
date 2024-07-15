	n_val = int(n * val)
	n_train = n - (n_test + n_val)

	idx = list(range(n))
	random.shuffle(idx)

	train_idx = idx[:n_train]
	val_idx = idx[n_train:(n_train + n_val)]
	test_idx = idx[(n_train + n_val):]

	train_set = np.array([X[ix] for ix in train_idx]), np.array([y[ix] for ix in train_idx])
	val_set = np.array([X[ix] for ix in val_idx]), np.array([y[ix] for ix in val_idx])
	test_set = np.array([X[ix] for ix in test_idx]), np.array([y[ix] for ix in test_idx])

	return train_set, val_set, test_set


def restore_net(ckpt):
	with open(ckpt, 'rb') as f:
