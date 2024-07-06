# 	num_classes = params["num_classes"]
#
# 	confusion = np.zeros((num_classes, num_classes))
# 	for iteration, (steps, targets, _) in enumerate(tqdm(val_loader)):
# 		if params["use_cuda"]:
# 			steps = steps.cuda()
# 			targets = targets.cuda()
#
