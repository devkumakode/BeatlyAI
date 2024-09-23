        #print(self.alpha.shape)
        #print(self.mask.shape)
        w_bin = torch.sum(self.B.float()*(self.alpha*self.mask.float()),dim=2)
        #print(w_bin)
        #print(tensor_shape)
        if self.structure == 'kernelwise':
            return w_bin.reshape(self.tensor_shape)
