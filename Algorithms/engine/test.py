					plot_window=plot_ecg_windows_size,
					max_plots=3
				)

		print("{} ACC: {:.4f}".format('testing', right / total))

		return ecgs, labels_list, predicted_list


