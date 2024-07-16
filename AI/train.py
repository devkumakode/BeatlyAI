    with torch.no_grad():
        maxk = max(topk)
        _, pred = output.topk(maxk, 1, True, True)
        pred = pred.t()
        correct = pred.eq(target.view(1, -1).expand_as(pred))

        for (i,k) in enumerate(topk):
            correct_sum[i] += (correct[:k].contiguous().view(-1).float().sum(0, keepdim=True)).item()
        return 


def get_accuracy(net, train_loader, loss_func):
    """Get the training loss and training accuracy."""
    net.eval()
    with torch.no_grad():
        train_loss = 0.
        num_batches = 0
