        elif self.structure == 'pixelwise':
            all_disc_w = torch.matmul(self.bit_table.view((1,1,self.bit_table.size(0),self.bit_table.size(1))).float(),self.alpha)
            ind_opt = torch.argmin(torch.abs(torch.transpose(target_w.view((self.tensor_shape[0],self.tensor_shape[1],1,-1)), 1,3) - all_disc_w), dim=2)
            self.B = torch.transpose((self.bit_table[ind_opt.view(-1),:]).view(self.tensor_shape[0],self.tensor_shape[2]*self.tensor_shape[3],self.tensor_shape[1],self.max_bit), 2,3)
            self.B *= self.mask.char()
        elif self.structure == 'channelwise':
            all_disc_w = torch.matmul(self.bit_table.view((1,1,self.bit_table.size(0),self.bit_table.size(1))).float(),self.alpha)
            ind_opt = torch.argmin(torch.abs(target_w.view((self.tensor_shape[0],1,1,-1)) - all_disc_w), dim=2)
            self.B = torch.transpose((self.bit_table[ind_opt.view(-1),:]).view(self.tensor_shape[0],1,self.tensor_shape[1]*self.tensor_shape[2]*self.tensor_shape[3],self.max_bit), 2,3)
            self.B *= self.mask.char()
        return True
            
    def speedup(self, pseudo_grad, pseudo_hessian):
        """Speed up the optimization on binary bases, i.e. take a following optimization step on coordinates while fixing binary bases. 
        """
        revised_grad_w = -pseudo_hessian*self.w_FP+pseudo_grad
