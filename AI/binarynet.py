

def transform_bin_basis(w_vec, max_dim, rel_norm_thres=REL_NORM_THRES):
    """Transform a full precision weight vector into multi-bit form, i.e. binary bases and coordiantes."""
    # Reshape the coordinates vector in w domain
    crd_w = w_vec.detach().view(-1,1) # 展开成一个列向量
    #print(crd_w)    
    # Get the dimensionality in w domain
    dim_w = crd_w.nelement()  #列向量的长度（16）
    #print(dim_w)
    # Determine the max number of dimensionality in alpha domain
    if dim_w <= max_dim:
        max_dim_alpha = dim_w
    else:
        max_dim_alpha = max_dim
    # Initialize binary basis matrix in alpha domain
    bin_basis_alpha = torch.zeros((dim_w, max_dim_alpha))
