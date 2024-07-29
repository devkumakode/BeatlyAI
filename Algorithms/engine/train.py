    return net


def train_test(data_loader, str1, step, net, device, batch_size):
    with torch.no_grad():
        right = 0.0
        total = 0.0
        net.eval()
        for sample in data_loader:

            ecgs = sample['ecg']
            labels = sample['label']

            ecgs = ecgs.to(device)
            labels = labels.to(device)

            if ecgs.shape[0] < batch_size:
