
	return res


def split_ecg_label_by_window (ecg, window=200):
	tmp = [x for x in np.array_split(np.array(ecg), int(len(ecg) / window)) if x.size > 0]
	res = np.zeros((len(tmp), window,))

	for ix in range(len(tmp)):
		if len(tmp[ix]) // window:
			tmp[ix] = tmp[ix][:window]
		res[ix] = np.array(tmp[ix]).reshape((window,))
