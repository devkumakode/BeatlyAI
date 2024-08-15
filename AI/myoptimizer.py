    def step(self, params_bin, mode, pruning_rate=None, closure=None):
        loss = None
        if closure is not None:
            loss = closure()
        
        for group in self.param_groups:
            # Check if this is a pruning step
            if pruning_rate is not None:
                importance_list = torch.tensor([])
            
            for i, (p_bin, p) in enumerate(zip(params_bin, group['params'])):
                if p.grad is None:
                    continue
                
                # Compute the gradient in both w domain and alpha domain
                grad = p.grad.data
                grad_alpha = p_bin.construct_grad_alpha(grad)
                state = self.state[p]
                
