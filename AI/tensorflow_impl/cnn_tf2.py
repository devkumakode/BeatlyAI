
        # Splitting the dataset into train and test datasets
        res = train_test_split(dataset, label_data,
                               test_size=validation_size, shuffle=True,
                               stratify=label_data)

        self.X_train, self.X_test, self.Y_train, self.Y_test = res

