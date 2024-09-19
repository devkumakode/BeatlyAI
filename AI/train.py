                #print(len(parameters_w))
                print(structure[i])
                parameters_w_bin.append(ConvLayer_bin(param.data, len(parameters_w)-1, structure[i], max_bit[i]))    
                i += 1
                tmp_param = param.detach()
                tmp_param.zero_().add_(parameters_w_bin[-1].reconstruct_w())    
        # Maintain other parameters (e.g. bias, batch normalization) in full precision 
        else:
            parameters_b.append(param)
