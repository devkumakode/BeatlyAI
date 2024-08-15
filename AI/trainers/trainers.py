        model = getattr(models2d, self.config["model"])(
            num_classes=self.config["num_classes"],
        )
        model = model.to(self.config["device"])
        return model

    def _init_dataloaders(self):
        train_loader = EcgDataset2D(
            self.config["train_json"], self.config["mapping_json"],
        ).get_dataloader(
            batch_size=self.config["batch_size"],
            num_workers=self.config["num_workers"],
        )
        val_loader = EcgDataset2D(
            self.config["val_json"], self.config["mapping_json"],
