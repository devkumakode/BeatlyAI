        self.mask.view(-1)[self.mask.view(-1).nonzero().view(-1)[ind_prune]]=0   
        self.B *= self.mask.char()
        self.alpha *= self.mask.float()  
        self.num_bin_filter = torch.sum(self.mask)  
        self.avg_bit = self.num_bin_filter.float()/(self.mask.size(0)*self.mask.size(1))
        if num_bin_filter_-self.num_bin_filter != ind_prune.size(0):
            print('wrong pruning')
            return False
        return True
        
    def optimize_bin_basis(self, pseudo_grad, pseudo_hessian):
        """Take one optimization step on the binary bases of this layer while fixing coordinates.
        """
        # Compute the target weight tensor, i.e. the optimal point in w domain according to the quadratic model function 
        target_w = self.w_FP-pseudo_grad/pseudo_hessian
        if self.structure == 'kernelwise':
            all_disc_w = torch.matmul(self.bit_table.view((1,1,self.bit_table.size(0),self.bit_table.size(1))).float(),self.alpha)
            ind_opt = torch.argmin(torch.abs(target_w.view((self.tensor_shape[0],self.tensor_shape[1],1,-1)) - all_disc_w), dim=2)
            self.B = torch.transpose((self.bit_table[ind_opt.view(-1),:]).view(self.tensor_shape[0],self.tensor_shape[1],self.tensor_shape[2],self.max_bit), 2,3)
            self.B *= self.mask.char()
