                    alpha[k,q,:dim,0] = crd
            elif self.structure == 'pixelwise':
                for h in range(self.tensor_shape[2]):
                    for w in range(self.tensor_shape[3]):
                        bin_basis, crd, dim = transform_bin_basis(w_cpu[k,:,w].view(-1), self.max_bit)
                        mask[k,h*self.tensor_shape[3]+w,:dim,0] = 1
                        B[k,h*self.tensor_shape[3]+w,:dim,:] = torch.t(bin_basis)
                        alpha[k,h*self.tensor_shape[3]+w,:dim,0] = crd
            if self.structure == 'channelwise':
                bin_basis, crd, dim = transform_bin_basis(w_cpu[k,:,:,:].view(-1), self.max_bit)
                mask[k,0,:dim,0] = 1
                B[k,0,:dim,:] = torch.t(bin_basis)
                alpha[k,0,:dim,0] = crd
        return B.to('cuda'), alpha.to('cuda'), mask.to('cuda')

    def reconstruct_w(self):
        """Reconstruct the weight tensor from the current quantization.
        Return the reconstructed weight tensor of this layer, i.e. \hat{w}.
        """
