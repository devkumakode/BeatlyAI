    # Initialize coordinates vector in alpha domain
    crd_alpha = torch.zeros(max_dim_alpha) 
    res = crd_w.detach()
    res_L2Norm_square = torch.sum(torch.pow(res,2))
    ori_L2Norm_square = torch.sum(torch.pow(crd_w,2))  
    for i in range(max_dim_alpha):
        if res_L2Norm_square/ori_L2Norm_square < rel_norm_thres:
            break
        new_bin_basis = binarize(res.view(-1))
        bin_basis_alpha[:,i] = new_bin_basis 
        B_ = bin_basis_alpha[:,:i+1]
        # Find the optimal coordinates in the space spanned by B_ 
        alpha_ = torch.mm(torch.inverse(torch.mm(torch.t(B_),B_)),torch.mm(torch.t(B_),crd_w)) 
        # Compute the residual (orthogonal to the space spanned by B_)
        res = crd_w - torch.mm(B_, alpha_)
        crd_alpha[:i+1] = alpha_.view(-1)
        res_L2Norm_square = torch.sum(torch.pow(res,2))   
    ind_neg = crd_alpha < 0
    crd_alpha[ind_neg] = -crd_alpha[ind_neg]
    bin_basis_alpha[:,ind_neg] = -bin_basis_alpha[:,ind_neg]
