        if self.exp_name is None:
            self.exp_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.log_dir = osp.join(self.config["exp_dir"], self.exp_name, "logs")
        self.pth_dir = osp.join(self.config["exp_dir"], self.exp_name, "checkpoints")
        os.makedirs(self.log_dir, exist_ok=True)
        os.makedirs(self.pth_dir, exist_ok=True)

        self.writer = SummaryWriter(log_dir=self.log_dir)

        self.model = self._init_net()
        self.optimizer = self._init_optimizer()
        self.criterion = nn.CrossEntropyLoss().to(self.config["device"])

