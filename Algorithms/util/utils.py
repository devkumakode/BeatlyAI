	plt.colorbar()

	if target_names is not None:
		tick_marks = np.arange(len(target_names))
		plt.xticks(tick_marks, target_names, rotation=45, size=19)
		plt.yticks(tick_marks, target_names, size=19)

	if normalize:
		cm = confusion_matrix.astype('float') / confusion_matrix.sum(axis=1)[:, np.newaxis]

	thresh = cm.max() / 1.5 if normalize else cm.max() / 2
	for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
		color = "white" if cm[i, j] > thresh else "black"
