

def test(net, test_loader, device, batch_size, plot_ecg=False, plot_ecg_windows_size=None):
	with torch.no_grad():
		ecgs_list = []
		labels_list = []
		predicted_list = []
		right = 0.0
		total = 0.0
		net.eval()
		for ix, sample in enumerate(test_loader):
			ecgs = sample['ecg']
			labels = sample['label']

			ecgs = ecgs.to(device)
			labels = labels.to(device)

			if ecgs.shape[0] < batch_size:
