
        else:
            self.training_epoch = 0
            self.total_iter = 0

        self.epochs = self.config.get("epochs", int(1e5))

    def _init_net(self):
        raise NotImplemented

    def _init_dataloaders(self):
        raise NotImplemented

