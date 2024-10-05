        if self.structure == 'kernelwise':
            revised_hessian = torch.matmul(self.B.float()*pseudo_hessian.view((self.tensor_shape[0],self.tensor_shape[1],1,-1)),torch.transpose(self.B,2,3).float())
            revised_hessian += torch.diag_embed(1+1e-6-(self.mask.float().squeeze(-1))) 
            revised_grad = torch.matmul(self.B.float(),revised_grad_w.view((self.tensor_shape[0],self.tensor_shape[1],-1,1)))
            self.alpha = -torch.matmul(torch.inverse(revised_hessian),revised_grad)
        elif self.structure == 'pixelwise':
            revised_hessian = torch.matmul(self.B.float()*torch.transpose(pseudo_hessian.view((self.tensor_shape[0],self.tensor_shape[1],1,-1)),1,3),torch.transpose(self.B,2,3).float())
            revised_hessian += torch.diag_embed(1+1e-6-(self.mask.float().squeeze(-1)))
            revised_grad = torch.matmul(self.B.float(),torch.transpose(revised_grad_w.view((self.tensor_shape[0],self.tensor_shape[1],-1,1)),1,2))
            self.alpha = -torch.matmul(torch.inverse(revised_hessian),revised_grad)
        elif self.structure == 'channelwise':
            revised_hessian = torch.matmul(self.B.float()*pseudo_hessian.view((self.tensor_shape[0],1,1,-1)),torch.transpose(self.B,2,3).float())
            revised_hessian += torch.diag_embed(1+1e-6-(self.mask.float().squeeze(-1))) 
            revised_grad = torch.matmul(self.B.float(),revised_grad_w.view((self.tensor_shape[0],1,-1,1)))
            self.alpha = -torch.matmul(torch.inverse(revised_hessian),revised_grad)
        self.alpha *= self.mask.float()
        ind_neg = self.alpha<0
        self.alpha[ind_neg] *= -1
        self.B.contiguous().view(-1,self.B.size(-1))[ind_neg.view(-1),:] *= -1
        self.num_bin_filter = torch.sum(self.mask)
        self.avg_bit = self.num_bin_filter.float()/(self.mask.size(0)*self.mask.size(1))
        return True
 
    
class FCLayer_bin(object):
    """This class defines the multi-bit form of the weight tensor of a convolutional layer used in ALQ. 

    Arguments:
        w_ori (float tensor): the 4-dim pretrained weight tensor of a convolutional layer.
        ind_layer (int): the index of this layer in the network.
        structure (string): the structure used for grouping the weights in this layer, optional values: 'subchannelwise'.
        max_bit (int): the maximum bitwidth used in initialization.
    """
    def __init__(self, w_ori, ind_layer, structure, num_subchannel, max_bit):
        # The layer type
        self.layer_type = 'fc'
        # The shape of the weight tensor of this layer
        self.tensor_shape = w_ori.size()
        # The maintained full precision weight tensor of this layer used in STE
        self.w_FP = w_ori.clone().to('cuda')
        # The index of this layer in the network
        self.ind_layer = ind_layer
        # The structure used for grouping the weights in this layer
        self.structure = structure
        # The maximum bitwidth used in initialization
        self.max_bit = max_bit
        # The number of groups in each channel, i.e. the number of subchannels 
        self.num_subchannel = num_subchannel
        # The number of weights in each subchannel
        self.num_w_subc = int(self.tensor_shape[1]/self.num_subchannel)
        # The binary bases, the coordinates, and the mask (only for parallel computing purposes) of each group
        self.B, self.alpha, self.mask = self.structured_sketch()
        # The total number of binary filters in this layer, namely the total number of (valid) alpha's
        self.num_bin_filter = torch.sum(self.mask)
        # The average bitwidth of this layer
        self.avg_bit = self.num_bin_filter.float()/(self.mask.size(0)*self.mask.size(1))
        # The total number of weights of this layer
        self.num_weight = self.w_FP.nelement()
        # The used look-up-table for bitwise values
        self.bit_table = construct_bit_table(self.max_bit)
        
    def structured_sketch(self):
        """Initialize the weight tensor using structured sketching. 
        Namely, structure the weights in groupwise, and quantize each group's weights in multi-bit form w.r.t. the reconstruction error.
        Return the binary bases, the coordinates, and the mask (only for parallel computing purposes) of each group. 
        """
        w_cpu = self.w_FP.to('cpu')
        B = torch.zeros((self.tensor_shape[0],self.num_subchannel,self.max_bit,self.num_w_subc)).to(torch.int8)
        alpha = torch.zeros((self.tensor_shape[0],self.num_subchannel,self.max_bit,1)).to(torch.float32)
        mask =  torch.zeros((self.tensor_shape[0],self.num_subchannel,self.max_bit,1)).to(torch.bool)
        for k in range(self.tensor_shape[0]):
            for (q,i) in enumerate(range(0,self.tensor_shape[1],self.num_w_subc)):
                bin_basis, crd, dim = transform_bin_basis(w_cpu[k,i:i+self.num_w_subc].view(-1), self.max_bit)
                mask[k,q,:dim,0] = 1
                B[k,q,:dim,:] = torch.t(bin_basis)
                alpha[k,q,:dim,0] = crd
        return B.to('cuda'), alpha.to('cuda'), mask.to('cuda')

    def reconstruct_w(self):
