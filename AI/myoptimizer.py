                    # Update the maintained full precision weights
                    p_bin.update_w_FP(-pseudo_grad/pseudo_hessian)
                    # Reconstruct the weight tensor from the current quantization
                    tmp_p = p.detach()
                    tmp_p.zero_().add_(p_bin.reconstruct_w())

                    # Update the state parameters in alpha domain (approximately)
                    state['step_alpha'] += 1
                    state['exp_avg_alpha'] = p_bin.construct_grad_alpha(exp_avg)
                    state['exp_avg_sq_alpha'] = p_bin.construct_hessian_alpha(exp_avg_sq)
                    state['max_exp_avg_sq_alpha'] = p_bin.construct_hessian_alpha(max_exp_avg_sq)
