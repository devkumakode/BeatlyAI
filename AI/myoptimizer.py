                    bias_correction1 = 1 - beta1 ** state['step']
                    bias_correction2 = 1 - beta2 ** state['step']

                    # Compute the pseudo gradient and the pseudo diagonal Hessian 
                    pseudo_grad = (group['lr'] / bias_correction1) * exp_avg 
                    pseudo_hessian = denom.div(math.sqrt(bias_correction2))
                    # Take one optimization step on binary bases
                    p_bin.optimize_bin_basis(pseudo_grad, pseudo_hessian)
                    # Speed up with an optimization step on coordinates
                    p_bin.speedup(pseudo_grad, pseudo_hessian)
                    # Reconstruct the weight tensor from the current quantization
                    p_bin.update_w_FP()
                    tmp_p = p.detach()
