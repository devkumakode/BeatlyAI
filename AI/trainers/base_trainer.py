        pd_class = np.empty(0)

        for i, batch in enumerate(self.train_loader):
            inputs = batch["image"].to(self.config["device"])
            targets = batch["class"].to(self.config["device"])

            predictions = self.model(inputs)
            loss = self.criterion(predictions, targets)

            classes = predictions.topk(k=1)[1].view(-1).cpu().numpy()

            gt_class = np.concatenate((gt_class, batch["class"].numpy()))
            pd_class = np.concatenate((pd_class, classes))

            total_loss += loss.item()

            self.optimizer.zero_grad()
