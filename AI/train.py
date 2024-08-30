        train_loss += loss.data.item()
        num_batches += 1   
    print("epoch: ", epoch, ", training loss: ", train_loss/num_batches)                
    print('training accuracy: ', [ci/total for ci in correct_sum])


def train_basis_STE(net, train_loader, loss_func, optimizer_w, optimizer_b, parameters_w_bin, epoch):
    """Train the binary bases (with speedup) by STE for one epoch."""
    net.train()
    train_loss = 0.
    num_batches = 0
    correct_sum = [0. for i in range(len(TOPK))]
