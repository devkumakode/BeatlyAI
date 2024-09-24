    net.eval()
    train_loss = 0.
    num_batches = 0
    correct_sum = [0. for i in range(len(TOPK))]
    total = 0
    for (inputs, labels) in train_loader:               
        inputs, labels = inputs.cuda(non_blocking=True), labels.cuda(non_blocking=True)
        outputs = net(inputs)
        loss = loss_func(outputs, labels)
        accuracy(outputs, labels, correct_sum, topk=TOPK)
        total += labels.size(0)
        train_loss += loss.data.item()
        num_batches += 1
    print('train loss: ', train_loss/num_batches)
    print('train accuracy: ', [ci/total for ci in correct_sum]) 
    num_weight_layer = 0.
    num_bit_layer = 0.
