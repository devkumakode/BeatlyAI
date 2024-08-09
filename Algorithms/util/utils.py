				size=23
			)

	plt.tight_layout()
	plt.ylabel('True label', size=23)
	plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass), size=23)
	plt.show()
