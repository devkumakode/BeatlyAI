        Namely, structure the weights in groupwise, and quantize each group's weights in multi-bit form w.r.t. the reconstruction error.
        Return the binary bases, the coordinates, and the mask (only for parallel computing purposes) of each group. 
        """
        w_cpu = self.w_FP.to('cpu')
        if self.structure == 'kernelwise':
            B = torch.zeros((self.tensor_shape[0],self.tensor_shape[1],self.max_bit,self.tensor_shape[2])).to(torch.int8)
            alpha = torch.zeros((self.tensor_shape[0],self.tensor_shape[1],self.max_bit,1)).to(torch.float32)
            mask =  torch.zeros((self.tensor_shape[0],self.tensor_shape[1],self.max_bit,1)).to(torch.bool)
