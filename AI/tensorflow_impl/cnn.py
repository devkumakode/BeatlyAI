        self.saver = ModelSaver(save_dir="saved_models/cnn/")

        logs_path = "tensorboard_data/cnn/"
        self.tensorboard_handler = TensorBoardHandler(logs_path)
        self.tensorboard_handler.add_histograms(self.weights)
        self.tensorboard_handler.add_histograms(self.biases)

        self.build()

    def build(self):
        dataset_len = []
        for dataset in self.datasets:
            dataset_len.append(len(dataset))

        validation_size = int(0.1 * sum(dataset_len))

