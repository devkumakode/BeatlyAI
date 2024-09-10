                )

        if osp.exists(self.config["ecg_data"] + ".atr"):
            ann = wfdb.rdann(self.config["ecg_data"], extension="atr")
            for label, peak in zip(ann.symbol, ann.sample):
                if peak < len(self.pipeline_loader.dataset.signal) and label != "N":
                    annotations.append(
                        {
                            "x": peak,
                            "y": self.pipeline_loader.dataset.signal[peak] - 0.1,
                            "text": label,
                            "xref": "x",
                            "yref": "y",
