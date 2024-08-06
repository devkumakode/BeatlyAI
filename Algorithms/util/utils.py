	cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
				  see http://matplotlib.org/examples/color/colormaps_reference.html
				  plt.get_cmap('jet') or plt.cm.Blues

	normalize:    If False, plot the raw numbers
				  If True, plot the proportions

	Usage
	-----
	plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
															  # sklearn.metrics.confusion_matrix
						  normalize    = True,                # show proportions
						  target_names = y_labels_vals,       # list of names of the classes
						  title        = best_estimator_name) # title of graph

