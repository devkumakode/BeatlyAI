        elif self.structure == 'pixelwise':
            B = torch.zeros((self.tensor_shape[0],self.tensor_shape[2],self.max_bit,self.tensor_shape[1])).to(torch.int8)
            alpha = torch.zeros((self.tensor_shape[0],self.tensor_shape[2],self.max_bit,1)).to(torch.float32)
            mask =  torch.zeros((self.tensor_shape[0],self.tensor_shape[2],self.max_bit,1)).to(torch.bool)
        elif self.structure == 'channelwise':
            B = torch.zeros((self.tensor_shape[0],1,self.max_bit,self.tensor_shape[1]*self.tensor_shape[2])).to(torch.int8)
            alpha = torch.zeros((self.tensor_shape[0],1,self.max_bit)).to(torch.float32)
            mask =  torch.zeros((self.tensor_shape[0],1,self.max_bit)).to(torch.bool)
        for k in range(self.tensor_shape[0]):
            if self.structure == 'kernelwise':
                for q in range(self.tensor_shape[1]):
                    bin_basis, crd, dim = transform_bin_basis(w_cpu[k,q,:].view(-1), self.max_bit)
                    #print(crd) # tensor([0.0030, 0.0093, 0.0231, 0.0371, 0.0655, 0.1454])
                    #print(dim) # tensor(6)
                    mask[k,q,:dim,0] = 1
                    #print(B.shape) # torch.Size([8, 1, 6, 16])
                    #print(t(bin_basis).shape)    ## 这里我进行了改动
                    #print(torch.t(bin_basis).shape) # torch.Size([6, 16])
                    B[k,q,:dim,:] = torch.t(bin_basis)
                    #print(alpha.shape)
