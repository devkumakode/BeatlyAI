	fss = set()
	max_ecg_raw_value = -np.inf
	min_ecg_raw_value = np.inf
	total_length = 0
	for index, row in df.iterrows():
		json_filename = os.path.join(config.ECG_DATA_DIR, row['name'])
		json_data = load_json(json_filename)

		ecg = json_data['data'][row['filename']]['ecg'][0]
		fs = json_data['data'][row['filename']]['fs']

		if max(ecg) > max_ecg_raw_value:
			max_ecg_raw_value = max(ecg)
		if min(ecg) < min_ecg_raw_value:
			min_ecg_raw_value = min(ecg)

		total_length += len(ecg)
		patients.add(row['Patient'])
		leads.add(row['Lead'])
		ecgs.append(len(ecg))
