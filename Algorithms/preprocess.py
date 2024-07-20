		fss.add(fs)

	print('Number of ECG leads: ', len(df.values.tolist()))
	print('Number of distinct patients: ', len(patients))
	print('Distinct sampling rates: ', fss)
	print('Number of lead types: ', len(leads))
	print('Max size of ECG: ', max(ecgs))
	print('Min size of ECG: ', min(ecgs))
	print('Mean size of ECG: ', np.mean(ecgs))
	print('Distinct sizes of ECG: ', set(ecgs))
	print('Max raw value of ECG: ', max_ecg_raw_value)
	print('Min raw value of ECG: ', min_ecg_raw_value)
	print('Total length in database: ', total_length)


def preprocess (df, window_len):
	x_data = np.empty((1, window_len, 1))
	y_data = np.zeros((1, window_len,))

	for index, row in df.iterrows():
