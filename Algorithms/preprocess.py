				ddde = 5
			c = np.dstack((a, b)).reshape((ecg_lead_splitted.shape[0], 220, 2))
		except ValueError:
			saa = 5

		ecg_label_splitted = split_ecg_label_by_window(ecg_labels, window=window_len)

		x_data = np.vstack((x_data, c))
		y_data = np.vstack((y_data, ecg_label_splitted))

	return x_data, y_data


def fun (df, mask_lambda, window_len=200, bwr=False):
	masked_df = df[mask_lambda]

	if bwr:
