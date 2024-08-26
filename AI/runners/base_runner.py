
        gt_class = np.empty(0)
        pd_class = np.empty(0)

        with torch.no_grad():
            for i, batch in tqdm(enumerate(self.inference_loader)):
                inputs = batch["image"].to(self.config["device"])
