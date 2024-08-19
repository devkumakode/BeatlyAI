        raise NotImplemented

    def run_pipeline(self):
        self.model.eval()
        pd_class = np.empty(0)
