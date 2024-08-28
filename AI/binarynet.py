    # Get the valid dimensionality in alpha domain
    dim_alpha = torch.sum(ind_valid) 
    sorted_ind = torch.argsort(crd_alpha[ind_valid])
    #print(dim_alpha)  #alpha 的长度 6
    #print(bin_basis_alpha)  # 二值化网络权重 二维tensor
    #print(ind_valid)
    #print(sorted_ind)
    if dim_alpha == 0:
        return [], [], 0
    else:
        return bin_basis_alpha[:,ind_valid][:,sorted_ind].to(torch.int8), crd_alpha[ind_valid][sorted_ind], dim_alpha


class ConvLayer_bin(object):
    """This class defines the multi-bit form of the weight tensor of a convolutional layer used in ALQ. 

    Arguments:
