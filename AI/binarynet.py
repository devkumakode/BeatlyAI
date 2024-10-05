        """Reconstruct the weight tensor from the current quantization.
        Return the reconstructed weight tensor of this layer, i.e. \hat{w}.
        """
        w_bin = torch.sum(self.B.float()*(self.alpha*self.mask.float()),dim=2)
        return w_bin.reshape(self.tensor_shape)
    
    def update_w_FP(self, w_FP_new=None):
        """Update the full precision weight tensor.
        In STE with loss-aware optimization, w_FP is the maintained full precision weight tensor.
        In ALQ optimization, w_FP is used to store the reconstructed weight tensor from the current quantization. 
        """
        if w_FP_new is not None:
            self.w_FP.add_(w_FP_new)
        else:
            self.w_FP.zero_().add_(self.reconstruct_w())        
    
    def construct_grad_alpha(self, grad_w):
        """Compute and return the gradient (or the first momentum) in alpha domain w.r.t the loss.
        """
        return torch.matmul(self.B.float(), grad_w.reshape((self.tensor_shape[0],self.num_subchannel,self.num_w_subc,1)))*self.mask.float()
        
    def construct_hessian_alpha(self, diag_hessian_w):
        """Compute and return the diagonal Hessian (or the second momentum) in alpha domain w.r.t the loss.
        """
        diag_hessian_alpha = torch.matmul(self.B.float()*diag_hessian_w.reshape((self.tensor_shape[0],self.num_subchannel,1,self.num_w_subc)), torch.transpose(self.B,2,3).float())
        return torch.diagonal(diag_hessian_alpha,dim1=-2,dim2=-1).unsqueeze(-1)*self.mask.float()
        
    def sort_importance_bin_filter(self, grad_alpha, diag_hessian_alpha, num_top):
        """Compute and sort the importance of binary filters (alpha's) in this layer.
        The importance is defined by the modeled loss increment caused by pruning each individual alpha.
        Return the selected num_top alpha's with the least importance.
        """
        delta_loss_prune = -grad_alpha*self.alpha+0.5*torch.pow(self.alpha,2)*diag_hessian_alpha
        sorted_ind = torch.argsort(delta_loss_prune[self.mask].view(-1))
        top_importance_list = torch.tensor([[self.ind_layer, sorted_ind[i], delta_loss_prune.view(-1)[sorted_ind[i]]] for i in range(num_top)])  
        return top_importance_list
                   
    def prune_alpha(self, ind_prune): 
        """Prune the cooresponding alpha's of this layer give the indexes.
