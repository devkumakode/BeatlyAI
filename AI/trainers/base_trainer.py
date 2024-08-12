        if pretrained_path:
            self.training_epoch, self.total_iter = load_checkpoint(
                pretrained_path, self.model, optimizer=self.optimizer,
            )
