def eval (ecgs, y_true, y_pred, labels, target_names, plot_acc=False, plot_loss=False, plot_conf_matrix=False, plot_ecg=False, plot_ecg_windows_size=None):

	if plot_acc:
		with open(config.RESOURCES_DIR + '/loss.pkl', 'rb') as f:
			loss = pickle.load(f)
			plot_learning_curve(loss, xlabel='Episode', ylabel='Loss')

	if plot_loss:
		with open(config.RESOURCES_DIR + '/accuracy.pkl', 'rb') as f:
			acc = pickle.load(f)
			plot_learning_curve(acc, xlabel='Episode', ylabel='Accuracy')

	# if plot_ecg:
	# 	visualise_ecg(
	# 		ecg=ecgs.numpy(),
	# 		labels=y_true.numpy(),
	# 		pred_vec=y_pred.numpy(),
	# 		plot_window=plot_ecg_windows_size,
	# 		max_plots=3
