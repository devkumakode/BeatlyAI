        self.num_bin_filter = torch.sum(self.mask)
        self.avg_bit = self.num_bin_filter.float()/(self.mask.size(0)*self.mask.size(1))
