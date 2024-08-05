		ecg = load_json(filename)

		ecg_lead = ecg['data'][ecg_csv_name]['ecg'][0]
		ecg_labels = ecg['data'][ecg_csv_name]['label'][0]
		fs = ecg['data'][ecg_csv_name]['fs']

		assert len(ecg_lead) == len(ecg_labels)

		ecg_lead_splitted = split_ecg_lead_by_window(ecg_lead, window=window_len)
		try:
