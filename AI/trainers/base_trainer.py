        with torch.no_grad():
            for i, batch in tqdm(enumerate(self.val_loader)):
                inputs = batch["image"].to(self.config["device"])
                targets = batch["class"].to(self.config["device"])

                predictions = self.model(inputs)
                loss = self.criterion(predictions, targets)

                classes = predictions.topk(k=1)[1].view(-1).cpu().numpy()

                gt_class = np.concatenate((gt_class, batch["class"].numpy()))
                pd_class = np.concatenate((pd_class, classes))

                total_loss += loss.item()

        total_loss /= len(self.val_loader)
        class_accuracy = sum(pd_class == gt_class) / pd_class.shape[0]
