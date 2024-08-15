    def _init_optimizer(self):
        optimizer = getattr(optim, self.config["optim"])(
            self.model.parameters(), **self.config["optim_params"]
        )
        return optimizer

    def train_epoch(self):
        self.model.train()
        total_loss = 0

        gt_class = np.empty(0)
