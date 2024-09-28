        else:
            self.w_FP.zero_().add_(self.reconstruct_w())

    def construct_grad_alpha(self, grad_w):
        """Compute and return the gradient (or the first momentum) in alpha domain w.r.t the loss.
        """
        if self.structure == 'kernelwise':
            return torch.matmul(self.B.float(), grad_w.reshape((self.tensor_shape[0],self.tensor_shape[1],-1,1)))*self.mask.float()
        elif self.structure == 'pixelwise':
            return torch.matmul(self.B.float(), torch.transpose(grad_w.reshape((self.tensor_shape[0],self.tensor_shape[1],-1,1)), 1,2) )*self.mask.float()
        elif self.structure == 'channelwise':
            return torch.matmul(self.B.float(), grad_w.reshape((self.tensor_shape[0],1,-1,1)))*self.mask.float()

    def construct_hessian_alpha(self, diag_hessian_w):
        """Compute and return the diagonal Hessian (or the second momentum) in alpha domain w.r.t the loss.
        """
        if self.structure == 'kernelwise':
            diag_hessian = torch.matmul(self.B.float()*diag_hessian_w.reshape((self.tensor_shape[0],self.tensor_shape[1],1,-1)), torch.transpose(self.B,2,3).float())
            return torch.diagonal(diag_hessian,dim1=-2,dim2=-1).unsqueeze(-1)*self.mask.float()
        elif self.structure == 'pixelwise':
