            self.optimizer.zero_grad()
            signal, label = [d.to(self.config.device) for d in data]
            prediction = self.model(einops.rearrange(signal, "b c e -> b e c"))
            loss = self.loss(prediction, label)
            loss.backward()
            self.optimizer.step()
