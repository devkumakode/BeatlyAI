            num_workers=self.config["num_workers"],
            shuffle=False,
        )

        return inference_loader
