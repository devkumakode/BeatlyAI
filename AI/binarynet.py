        # The layer type
        self.layer_type = 'conv'
        # The shape of the weight tensor of this layer
        self.tensor_shape = w_ori.size()
        # The maintained full precision weight tensor of this layer used in STE
        self.w_FP = w_ori.clone().to('cuda')
        # The index of this layer in the network
        self.ind_layer = ind_layer
        # The structure used for grouping the weights in this layer
        self.structure = structure
        # The maximum bitwidth used in initialization
        self.max_bit = max_bit
        # The binary bases, the coordinates, and the mask (only for parallel computing purposes) of each group
        self.B, self.alpha, self.mask = self.structured_sketch()
        # The total number of binary filters in this layer, namely the total number of (valid) alpha's
        self.num_bin_filter = torch.sum(self.mask)
        # The average bitwidth of this layer
        self.avg_bit = self.num_bin_filter.float()/(self.mask.size(0)*self.mask.size(1))
        # The total number of weights of this layer
        self.num_weight = self.w_FP.nelement()
