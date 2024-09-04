            loss.backward()
            self.optimizer.step()

            if (i + 1) % 10 == 0:
                print(
                    "\tIter [%d/%d] Loss: %.4f"
                    % (i + 1, len(self.train_loader), loss.item()),
                )

            self.writer.add_scalar(
                "Train loss (iterations)", loss.item(), self.total_iter,
