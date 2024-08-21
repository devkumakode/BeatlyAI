        return model

    def _init_dataloaders(self):
        train_loader = EcgDataset1D(
