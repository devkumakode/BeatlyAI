	import matplotlib.pyplot as plt
	import numpy as np
	import itertools

	accuracy = np.trace(confusion_matrix) / float(np.sum(confusion_matrix))
	misclass = 1 - accuracy

	if cmap is None:
		cmap = plt.get_cmap('Blues')

	plt.figure(figsize=(8, 6))
	plt.imshow(confusion_matrix, interpolation='nearest', cmap=cmap)
	plt.title(title)
