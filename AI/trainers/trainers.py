            self.config["train_json"], self.config["mapping_json"],
        ).get_dataloader(
            batch_size=self.config["batch_size"],
            num_workers=self.config["num_workers"],
        )
        val_loader = EcgDataset1D(
            self.config["val_json"], self.config["mapping_json"],
        ).get_dataloader(
            batch_size=self.config["batch_size"],
            num_workers=self.config["num_workers"],
