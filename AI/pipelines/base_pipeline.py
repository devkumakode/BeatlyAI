                peak < len(self.pipeline_loader.dataset.signal)
                and self.mapper[label] != "N"
            ):
                annotations.append(
                    {
                        "x": peak,
                        "y": self.pipeline_loader.dataset.signal[peak],
                        "text": self.mapper[label],
                        "xref": "x",
                        "yref": "y",
