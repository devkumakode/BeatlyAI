                        tmp_p.zero_().add_(p_bin.w_FP.data)
                                     
                elif mode == 'basis':
                    # Update the state parameters in w domain
                    exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
                    max_exp_avg_sq = state['max_exp_avg_sq']
                    beta1, beta2 = group['betas']
                    state['step'] += 1
                    # Decay the first and second moment running average coefficient
                    exp_avg.mul_(beta1).add_(1 - beta1, grad)
                    exp_avg_sq.mul_(beta2).addcmul_(1 - beta2, grad, grad)
                    # Maintain the maximum of all second moment running avg. till now
                    torch.max(max_exp_avg_sq, exp_avg_sq, out=max_exp_avg_sq)
                    # Use the max. for normalizing running avg. of gradient
                    denom = max_exp_avg_sq.sqrt().add_(group['eps'])
