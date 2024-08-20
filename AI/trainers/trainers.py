        ).get_dataloader(
            batch_size=self.config["batch_size"],
            num_workers=self.config["num_workers"],
        )

        return train_loader, val_loader


class Trainer1D(BaseTrainer):
    def __init__(self, config):
        super().__init__(config)

    def _init_net(self):
        model = getattr(models1d, self.config["model"])(
            num_classes=self.config["num_classes"],
        )
        model = model.to(self.config["device"])
