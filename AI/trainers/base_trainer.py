        self.train_loader, self.val_loader = self._init_dataloaders()

        pretrained_path = self.config.get("model_path", False)
