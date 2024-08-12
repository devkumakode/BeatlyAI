        total += labels.size(0)
        train_loss += loss.data.item()
        num_batches += 1
    print("epoch: ", epoch, ", training loss: ", train_loss/num_batches)            
    print('training accuracy: ', [ci/total for ci in correct_sum])


def train_coordinate(net, train_loader, loss_func, optimizer_w, optimizer_b, parameters_w_bin, epoch):
    """Train the coordinates for one epoch."""
    net.train()
    train_loss = 0.
    num_batches = 0
    correct_sum = [0. for i in range(len(TOPK))]
    total = 0
    for (inputs, labels) in train_loader:               
        inputs, labels = inputs.cuda(non_blocking=True), labels.cuda(non_blocking=True)
        optimizer_w.zero_grad()
        optimizer_b.zero_grad()
