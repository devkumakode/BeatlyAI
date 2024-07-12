			_, predicted = torch.max(output.data, 1)
			label_true = labels.contiguous().view(-1).long()

			total += label_true.size(0)
			right += (predicted == label_true).sum().item()

			if ecgs.shape[0] == 32:
				ecgs_list.extend(ecgs.numpy())
				labels_list.extend(label_true.numpy())
				predicted_list.extend(predicted.numpy())

