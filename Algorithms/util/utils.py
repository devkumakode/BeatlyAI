		title='Distribution of ECG Signal',
		ax=None,
		stats=True
):
	mean = data.mean(skipna=True)
	std = data.std(skipna=True)

	if ax is None:
		fig, ax = plt.subplots()

	sns.distplot(data, bins=200, fit=norm, kde=True, ax=ax, norm_hist=True, hist=True)

	if stats:
		ax.axvline(mean.item(), color='w', linestyle='dashed', linewidth=2)
