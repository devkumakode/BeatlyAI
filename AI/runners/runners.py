        ).get_dataloader(
            batch_size=self.config["batch_size"],
            num_workers=self.config["num_workers"],
            shuffle=False,
        )

        return inference_loader


class Runner1D(BaseRunner):
