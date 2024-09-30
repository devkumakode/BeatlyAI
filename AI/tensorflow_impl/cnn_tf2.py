        # From the training dataset we further split it to obtain the validation dataset
        res = train_test_split(self.X_train, self.Y_train,
                               test_size=validation_size, stratify=self.Y_train)
