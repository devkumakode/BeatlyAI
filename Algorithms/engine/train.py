
            total = 0.0
            correct = 0.0

            ecgs = samples_batch['ecg']
            labels = samples_batch['label']
            target = labels.contiguous().view(-1).long()

            ecgs = ecgs.to(device)
