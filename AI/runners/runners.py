from dataloaders.dataset1d import EcgDataset1D
from dataloaders.dataset2d import EcgDataset2D
from models import models1d, models2d
from runners.base_runner import BaseRunner


class Runner2D(BaseRunner):
    def __init__(self, config):
        super().__init__(config)

    def _init_net(self):
        model = getattr(models2d, self.config["model"])(
            num_classes=self.config["num_classes"],
        )
        model = model.to(self.config["device"])
        return model

    def _init_dataloader(self):
        inference_loader = EcgDataset2D(
            self.config["json"], self.config["mapping_json"],
