            end = i
            plt.plot(np.arange(start, end+1), x[start:end+1], cmap[int(y[i])])
            start = i+1
    plt.show()


def train(net, train_loader, val_loader, epochs, criterion, optimizer, device, batch_size):
    loss_values_final = []
    accuracy_final = []

    for step in range(epochs):
        running_loss = 0.0
        net.train()
        net.to(device)

        loss_values = []
        accuracy = []

        for i, samples_batch in enumerate(train_loader):
