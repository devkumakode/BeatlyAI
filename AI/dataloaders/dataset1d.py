
    def get_dataloader(self, num_workers=4, batch_size=16, shuffle=True):
        data_loader = DataLoader(
            self, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers,
        )
        return data_loader

    def __len__(self):
        return len(self.peaks)
