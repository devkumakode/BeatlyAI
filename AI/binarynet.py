        elif self.structure == 'pixelwise':
            return torch.transpose(w_bin,1,2).reshape(self.tensor_shape)
        elif self.structure == 'channelwise':
            return w_bin.reshape(self.tensor_shape)

    def update_w_FP(self, w_FP_new=None):
        """Update the full precision weight tensor.
        In STE with loss-aware optimization, w_FP is the maintained full precision weight tensor.
        In ALQ optimization, w_FP is used to store the reconstructed weight tensor from the current quantization. 
        """
        if w_FP_new is not None:
            self.w_FP.add_(w_FP_new)
