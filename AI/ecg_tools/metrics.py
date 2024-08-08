        self.labels = []

    def update(self, prediction, label):
        prediction = prediction.tolist()
        label = label.tolist()
        self.predictions += prediction
        self.labels += label

    @property
    def sensitivity(self):
