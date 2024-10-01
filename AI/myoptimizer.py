                for i, (p_bin, p) in enumerate(zip(params_bin, group['params'])):
                    p_bin.prune_alpha((torch.sort(list_prune[list_prune[:,0]==i,1])[0]).to(torch.int64))
                    p_bin.update_w_FP()
                    tmp_p = p.detach()
                    tmp_p.zero_().add_(p_bin.w_FP.data)
        return loss
