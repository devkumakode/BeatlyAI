		ax.axvline(std.item(), color='r', linestyle='dashed', linewidth=2)
		ax.axvline(-std.item(), color='r', linestyle='dashed', linewidth=2)

	ax.set_xlabel("Samples")
	ax.set_ylabel("Probability density")
	ax.set_title(title)
	ax.text(-7, 0.1, "Extreme negatives")
	ax.text(7, 0.1, "Extreme positives")
