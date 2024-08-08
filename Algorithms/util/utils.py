				j, i, "{:0.4f}".format(cm[i, j]),
				horizontalalignment="center",
				color=color,
				size=23
			)
		else:
			plt.text(
				j, i, "{:,}".format(cm[i, j]),
				horizontalalignment="center",
				color=color,
