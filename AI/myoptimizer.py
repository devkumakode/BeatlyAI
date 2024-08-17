                    state['exp_avg_alpha'] = torch.zeros_like(p_bin.alpha)
                    state['exp_avg_sq_alpha'] = torch.zeros_like(p_bin.alpha)
                    state['max_exp_avg_sq_alpha'] = torch.zeros_like(p_bin.alpha)
                    
                    state['step'] = 0
                    state['exp_avg'] = torch.zeros_like(p.data)
                    state['exp_avg_sq'] = torch.zeros_like(p.data)
                    state['max_exp_avg_sq'] = torch.zeros_like(p.data)

                if mode == 'coordinate':
                    # Update the state parameters in w domain
                    exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
