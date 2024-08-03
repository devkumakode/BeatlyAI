
		assert len(ecg_lead) == len(ecg_labels)

		ecg_lead_splitted = split_ecg_lead_by_window(ecg_lead, window=window_len)
		ecg_label_splitted = split_ecg_label_by_window(ecg_labels, window=window_len)

		x_data = np.vstack((x_data, ecg_lead_splitted))
		y_data = np.vstack((y_data, ecg_label_splitted))
