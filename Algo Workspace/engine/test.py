		conf_mat = confusion_matrix.confusion_matrix(y_true=y_true, y_pred=y_pred, labels=labels)

		plot_confusion_matrix(
			confusion_matrix=conf_mat,
			target_names=target_names,
			title='Confusion matrix',
			normalize=True
		)

	report = classification_report(y_true=y_true, y_pred=y_pred, labels=labels, target_names=target_names)

	print('Report: ' + str(report))