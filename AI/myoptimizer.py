                    max_exp_avg_sq = state['max_exp_avg_sq']
                    beta1, beta2 = group['betas']
                    state['step'] += 1
                    # Decay the first and second moment running average coefficient
