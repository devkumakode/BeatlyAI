        self.alpha = -torch.matmul(torch.inverse(revised_hessian),revised_grad)
        self.alpha *= self.mask.float()
        ind_neg = self.alpha<0
        self.alpha[ind_neg] *= -1
        self.B.contiguous().view(-1,self.B.size(-1))[ind_neg.view(-1),:] *= -1
