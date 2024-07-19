        return self.samples
    

# ECG dataset
train_dataset = ECGDataSet(split='train')
validate_dataset = ECGDataSet(split='validate')

# data loader
# It allows you to efficiently load and iterate over batches of data during the training or evaluation process.
train_dataloader = DataLoader(dataset=train_dataset, batch_size=128, shuffle=True, num_workers=20)
validate_dataloader = DataLoader(dataset=validate_dataset, batch_size=128, shuffle=False, num_workers=20)

