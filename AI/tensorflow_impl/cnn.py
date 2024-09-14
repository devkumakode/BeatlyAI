        # Shuffle the input, helps training
        concat_dataset = np.concatenate(self.datasets)
        concat_dataset, self.label_data = shuffle_tensors(concat_dataset, self.label_data)

        # split training and testing sets
        self.X_train, self.X_test = np.split(concat_dataset,
                                             [len(concat_dataset)-validation_size])

        self.Y_train, self.Y_test = np.split(self.label_data,
                                             [len(self.label_data)-validation_size])

        if verbose:
