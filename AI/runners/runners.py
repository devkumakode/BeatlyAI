    def __init__(self, config):
        super().__init__(config)

    def _init_net(self):
        model = getattr(models1d, self.config["model"])(
            num_classes=self.config["num_classes"],
        )
        model = model.to(self.config["device"])
        return model

    def _init_dataloader(self):
        inference_loader = EcgDataset1D(
