                    exp_avg_alpha.mul_(beta1).add_(1 - beta1, grad_alpha)
                    exp_avg_sq_alpha.mul_(beta2).addcmul_(1 - beta2, grad_alpha, grad_alpha)
                    # Maintain the maximum of all second moment running avg. till now
                    torch.max(max_exp_avg_sq_alpha, exp_avg_sq_alpha, out=max_exp_avg_sq_alpha)
                    # Use the max. for normalizing running avg. of gradient
                    denom_alpha = max_exp_avg_sq_alpha.sqrt().add_(group['eps'])
                    bias_correction1 = 1 - beta1 ** state['step_alpha']
                    bias_correction2 = 1 - beta2 ** state['step_alpha']

                    # Compute the pseudo gradient and the pseudo diagonal Hessian 
                    pseudo_grad_alpha = (group['lr'] / bias_correction1) * exp_avg_alpha 
                    pseudo_hessian_alpha = denom_alpha.div(math.sqrt(bias_correction2))
                    
                    # Check if this is a pruning step
                    if pruning_rate is not None:
                        # Compute the integer used to determine the number of selected alpha's in this layer
                        float_tmp = p_bin.num_bin_filter.item()*pruning_rate[0]
                        int_tmp = int(float_tmp)
