		val=.05,
		test=.2
):
	assert len(X) == len(y), 'Length of X and y must be the same'
	n = len(X)
	n_test = int(n * test)
