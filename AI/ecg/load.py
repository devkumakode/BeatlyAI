        x = (x - self.mean) / self.std
        x = x[:, :, None]
