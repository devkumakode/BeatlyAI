            
            # Check if this is a pruning step        
            if pruning_rate is not None:
                # Resort the importance of selected binary filters (alpha's) over all layers 
                sorted_ind = torch.argsort(importance_list[:,-1])
                # Compute the number of pruned alpha's in this iteration
                # Note that unlike the paper, M_p varies over iterations here, but this does not influence the pruning schedule. 
                M_p = int(sorted_ind.nelement()*pruning_rate[1])
                # Determine indexes of alpha's to be pruned
                ind_prune = sorted_ind[:M_p]
                list_prune = importance_list[ind_prune,:]
                # Prune alpha's in each layer and reconstruct the weight tensor
