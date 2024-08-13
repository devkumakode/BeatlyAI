        self.res_dir = osp.join(self.config["exp_dir"], self.exp_name, "results")
        os.makedirs(self.res_dir, exist_ok=True)

        self.model = self._init_net()
