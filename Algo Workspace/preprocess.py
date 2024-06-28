	train_set, val_set, test_set = train_val_test_data_split(x_train, y_train)

	print('train set: ', train_set[0].shape, train_set[1].shape)
	print('val set: ', val_set[0].shape, val_set[1].shape)
	print('test set: ', test_set[0].shape, test_set[1].shape)

	if SAVE_TO_FILE:
		save_as_pkl('/train_set_bwr.pkl', train_set)
		save_as_pkl('/val_set_bwr.pkl', val_set)
		save_as_pkl('/test_set_bwr.pkl', test_set)
