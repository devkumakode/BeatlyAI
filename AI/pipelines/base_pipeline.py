
        self.pipeline_loader = self._init_dataloader()

        self.mapper = json.load(open(config["mapping_json"]))
        self.mapper = {j: i for i, j in self.mapper.items()}

        pretrained_path = self.config.get("model_path", False)
        if pretrained_path:
            load_checkpoint(pretrained_path, self.model)
        else:
            raise Exception(
                "model_path doesnt't exist in config. Please specify checkpoint path",
            )

    def _init_net(self):
        raise NotImplemented

    def _init_dataloader(self):
