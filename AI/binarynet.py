        self.B *= self.mask.char()
        return True
                               
    def speedup(self, pseudo_grad, pseudo_hessian):
        """Speed up the optimization on binary bases, i.e. take a following optimization step on coordinates while fixing binary bases. 
        """
        revised_grad_w = -pseudo_hessian*self.w_FP+pseudo_grad
        revised_hessian = torch.matmul(self.B.float()*pseudo_hessian.view((self.tensor_shape[0],self.num_subchannel,1,-1)),torch.transpose(self.B,2,3).float())
        revised_hessian += torch.diag_embed(1+1e-6-(self.mask.float().squeeze(-1))) 
        revised_grad = torch.matmul(self.B.float(),revised_grad_w.view((self.tensor_shape[0],self.num_subchannel,-1,1)))
