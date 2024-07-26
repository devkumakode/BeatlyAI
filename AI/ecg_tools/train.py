            signal_length=config.model.signal_length,
            expansion=config.model.expansion,
            input_channels=config.model.input_channels
        ).to(config.device)
        self.config = config
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=self.config.lr, weight_decay=1e-4)
        self.loss = torch.nn.CrossEntropyLoss(weight=torch.tensor([0.1, 0.4, 0.2, 0.5, 0.2]).to(self.config.device))
        self.data_loader = get_data_loaders(self.config.dataset)
        self.metrics = {
            Mode.train: Metrics(),
            Mode.eval: Metrics()
        }

    def train(self):
        confusion_matrices_image_train, confusion_matrices_image_eval = [], []
        for epoch in range(self.config.num_epochs):
            confusion_matrices_image_train.append(self.train_epoch(epoch))

            if epoch % self.config.validation_frequency == 0:
