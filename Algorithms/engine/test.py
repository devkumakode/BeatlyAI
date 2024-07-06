# 		output = model(steps)
#
# 		rows = targets.cpu().numpy()
# 		cols = output.max(1)[1].cpu().numpy()
#
# 		confusion[rows, cols] += 1
#
# 		loss += criterion(output, targets)
#
# 	loss = loss / iteration
# 	acc = np.trace(confusion) / np.sum(confusion)
#
# 	# Plot confusion matrix in visdom
# 	logger.heatmap(confusion, win='4', opts=dict(
# 		title="Confusion_Matrix_epoch_{}".format(epoch),
# 		columnnames=["A","B","C","D","E"],
# 		rownames=["A","B","C","D","E"])
# 	)
#
# 	return loss, acc
