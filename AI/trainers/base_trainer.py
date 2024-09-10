            self.total_iter += 1

        total_loss /= len(self.train_loader)
        class_accuracy = sum(pd_class == gt_class) / pd_class.shape[0]

        print("Train loss - {:4f}".format(total_loss))
        print("Train CLASS accuracy - {:4f}".format(class_accuracy))

        self.writer.add_scalar("Train loss (epochs)", total_loss, self.training_epoch)
        self.writer.add_scalar(
            "Train CLASS accuracy", class_accuracy, self.training_epoch,
        )
