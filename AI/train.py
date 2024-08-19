def train_basis(net, train_loader, loss_func, optimizer_w, optimizer_b, parameters_w_bin, epoch):
    """Train the binary bases (with speedup) for one epoch."""
    net.train()
    train_loss = 0.
    num_batches = 0
    correct_sum = [0. for i in range(len(TOPK))]
    total = 0
    for inputs, labels in train_loader:               
        inputs, labels = inputs.cuda(non_blocking=True), labels.cuda(non_blocking=True)
        optimizer_w.zero_grad()
