                    exp_avg.mul_(beta1).add_(1 - beta1, grad)
                    exp_avg_sq.mul_(beta2).addcmul_(1 - beta2, grad, grad)
                    # Maintain the maximum of all second moment running avg. till now
                    torch.max(max_exp_avg_sq, exp_avg_sq, out=max_exp_avg_sq)

                    # Update the state parameters in alpha domain
                    exp_avg_alpha, exp_avg_sq_alpha = state['exp_avg_alpha'], state['exp_avg_sq_alpha']
                    max_exp_avg_sq_alpha = state['max_exp_avg_sq_alpha']
                    state['step_alpha'] += 1
                    # L2 regularization on coordinates (in alpha domain)
                    if group['weight_decay'] != 0:
                        grad_alpha = grad_alpha.add(p_bin.alpha, alpha=group['weight_decay'])
                    # Decay the first and second moment running average coefficient
