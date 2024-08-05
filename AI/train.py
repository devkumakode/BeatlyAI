        print('training accuracy: ', [ci/total for ci in correct_sum])


def train_fullprecision(net, train_loader, loss_func, optimizer, epoch):
    """Train the original full precision network for one epoch."""
    net.train()
