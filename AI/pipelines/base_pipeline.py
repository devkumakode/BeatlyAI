        pd_peaks = np.empty(0)

        with torch.no_grad():
            for i, batch in tqdm(enumerate(self.pipeline_loader)):
                inputs = batch["image"].to(self.config["device"])

                predictions = self.model(inputs)

                classes = predictions.topk(k=1)[1].view(-1).cpu().numpy()

                pd_class = np.concatenate((pd_class, classes))
                pd_peaks = np.concatenate((pd_peaks, batch["peak"]))

        pd_class = pd_class.astype(int)
        pd_peaks = pd_peaks.astype(int)

        annotations = []
        for label, peak in zip(pd_class, pd_peaks):
            if (
