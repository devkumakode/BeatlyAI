            diag_hessian = torch.matmul(self.B.float()*torch.transpose(diag_hessian_w.reshape((self.tensor_shape[0],self.tensor_shape[1],1,-1)), 1,3), torch.transpose(self.B,2,3).float())
            return torch.diagonal(diag_hessian,dim1=-2,dim2=-1).unsqueeze(-1)*self.mask.float()
        elif self.structure == 'channelwise':
            diag_hessian = torch.matmul(self.B.float()*diag_hessian_w.reshape((self.tensor_shape[0],1,1,-1)), torch.transpose(self.B,2,3).float())
            return torch.diagonal(diag_hessian,dim1=-2,dim2=-1).unsqueeze(-1)*self.mask.float()

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
        """
        num_bin_filter_ = torch.sum(self.mask)
