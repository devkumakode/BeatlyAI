                    # Compute the pseudo gradient and the pseudo diagonal Hessian 
                    pseudo_grad = (group['lr'] / bias_correction1) * exp_avg 
                    pseudo_hessian = denom.div(math.sqrt(bias_correction2))
                    
                    # Take one optimization step on binary bases
                    p_bin.optimize_bin_basis(pseudo_grad, pseudo_hessian)
                    # Speed up with an optimization step on coordinates
                    p_bin.speedup(pseudo_grad, pseudo_hessian)
