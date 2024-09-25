
def test(net, test_loader, loss_func):
    """Get the test loss and test accuracy."""
    net.eval()
    test_loss = 0.
    num_batches = 0
    correct_sum = [0. for i in range(len(TOPK))]
    total = 0
    with torch.no_grad():
        for (inputs, labels) in test_loader:
            inputs, labels = inputs.cuda(non_blocking=True), labels.cuda(non_blocking=True)
            outputs = net(inputs)
            loss = loss_func(outputs, labels)  
            accuracy(outputs, labels, correct_sum, topk=TOPK)
            total += labels.size(0)
            test_loss += loss.data.item()
            num_batches += 1
        print("test loss: ", test_loss/num_batches)
        print("test accuracy: ", [ci/total for ci in correct_sum])
