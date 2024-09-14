        if 'weight' in name and param.dim()>1:
            parameters_w.append(param)
            #print(param.dim())
            # Initialize fully connected layers (param.dim()==2)
            if 'fc' in name or 'classifier' in name:
                print(structure[i])
                parameters_w_bin.append(FCLayer_bin(param.data, len(parameters_w)-1, structure[i], num_subchannel[i], max_bit[i]))  
                i += 1
                tmp_param = param.detach()
                tmp_param.zero_().add_(parameters_w_bin[-1].reconstruct_w())
            # Initialize convolutional layers (param.dim()==3)
            else:
