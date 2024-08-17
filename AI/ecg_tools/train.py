        return confusion_matrices_image_train, confusion_matrices_image_eval

    def train_epoch(self, epoch):
        self.model.train()
        loader = tqdm(self.data_loader[Mode.train])
        accuracy = 0
        self.metrics[Mode.train].reset()
        for index, data in enumerate(loader):
