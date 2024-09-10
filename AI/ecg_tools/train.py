            accuracy += torch.sum(prediction.argmax(1) == label)
            self.metrics[Mode.train].update(prediction.argmax(1), label)
            loader.set_description(f"TRAINING: {epoch}, loss: {loss.item()}. Target: {label[:8].tolist()}, Prediction: {prediction.argmax(1)[:8].tolist()}")
        print(f"TRAINING Accuracy: {accuracy / len(loader) / self.config.dataset.batch_size}")
        print(self.metrics[Mode.train].confusion_matrix())
        return self.metrics[Mode.train].confusion_matrix_image()

    @torch.no_grad()
    def validate_epoch(self, epoch):
        self.model.eval()
        accuracy = 0
        loader = tqdm(self.data_loader[Mode.eval])
        self.metrics[Mode.eval].reset()
        for index, data in enumerate(loader):
            signal, label = [d.to(self.config.device) for d in data]
            prediction = self.model(einops.rearrange(signal, "b c e -> b e c"))
