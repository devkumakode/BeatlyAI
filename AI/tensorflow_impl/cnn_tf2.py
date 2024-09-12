
        self.set_data()
        self.define_model()

    def set_data(self):
        dataset_len = []
        for dataset in self.datasets:
            dataset_len.append(len(dataset))

        # validation on 10% of the training data
        validation_size = 0.1

        print("Validation percentage: {}%".format(validation_size*100))
        print("Total samples: {}".format(sum(dataset_len)))
        print("Heart diseases: {}".format(', '.join(heart_diseases)))

        concat_dataset = np.concatenate(self.datasets)
