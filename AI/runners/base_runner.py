
        self.model = self._init_net()

        self.inference_loader = self._init_dataloader()

        pretrained_path = self.config.get("model_path", False)
        if pretrained_path:
            load_checkpoint(pretrained_path, self.model)
        else:
            raise Exception(
