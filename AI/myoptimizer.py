                        if random.random()<float_tmp-int_tmp:
                            int_tmp += 1 
                        # Sort the importance of binary filters (alpha's) in this layer and select Top-k% (int_tmp) unimportant ones
                        p_bin_importance_list = p_bin.sort_importance_bin_filter(pseudo_grad_alpha, pseudo_hessian_alpha, int_tmp) 
                        importance_list = torch.cat((importance_list,p_bin_importance_list), 0) 
                    else:
                        # Take one optimization step on coordinates
                        p_bin.alpha.add_(-pseudo_grad_alpha/pseudo_hessian_alpha)
                        # Reconstruct the weight tensor from the current quantization
                        p_bin.update_w_FP()
                        tmp_p = p.detach()
