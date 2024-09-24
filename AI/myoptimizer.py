                    tmp_p.zero_().add_(p_bin.w_FP.data)

                    # Update the state parameters in alpha domain (approximately)
                    state['step_alpha'] += 1
                    state['exp_avg_alpha'] = p_bin.construct_grad_alpha(exp_avg)
                    state['exp_avg_sq_alpha'] = p_bin.construct_hessian_alpha(exp_avg_sq)
