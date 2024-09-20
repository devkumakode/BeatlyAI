
        print("Validation loss - {:4f}".format(total_loss))
        print("Validation CLASS accuracy - {:4f}".format(class_accuracy))

        self.writer.add_scalar("Validation loss", total_loss, self.training_epoch)
        self.writer.add_scalar(
            "Validation CLASS accuracy", class_accuracy, self.training_epoch,
        )

    def loop(self):
        for epoch in range(self.training_epoch, self.epochs):
            print("Epoch - {}".format(self.training_epoch + 1))
            self.train_epoch()
            save_checkpoint(
                {
