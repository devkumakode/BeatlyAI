        params (iterable): iterable of parameters to optimize or dicts defining parameter groups.
        lr (float, optional): learning rate (default: 1e-3).
        betas (Tuple[float, float], optional): coefficients used for computing running averages of gradient and its square (default: (0.9, 0.999)).
        eps (float, optional): term added to the denominator to improve numerical stability (default: 1e-8).
        weight_decay (float, optional): weight decay (L2 regularization) (default: 0).
        
    Reference:
        Adam optimizer by Pytorch:
        https://pytorch.org/docs/stable/_modules/torch/optim/adam.html#Adam
        On the Convergence of Adam and Beyond:
        https://openreview.net/forum?id=ryQu7f-RZ
    """
    
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0.):
        # Check the validity 
