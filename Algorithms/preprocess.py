			shape = ecg_lead_splitted.shape[0]*ecg_lead_splitted.shape[1]
			ecg_lead_splitted_filtered = np.array(
					BaselineWanderRemoval.fix_baseline_wander(ecg_lead_splitted.reshape((shape,)), sr=fs)
			).reshape((ecg_lead_splitted.shape[0], 220, 1))

			a = ecg_lead_splitted.reshape((shape,))
			b = ecg_lead_splitted_filtered.reshape((shape,))

			if ecg_lead_splitted.shape[0] > 1:
