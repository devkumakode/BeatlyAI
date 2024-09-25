    total = 0
    with torch.no_grad():
        for (inputs, labels) in val_loader:
            inputs, labels = inputs.cuda(non_blocking=True), labels.cuda(non_blocking=True)
            outputs = net(inputs)
            loss = loss_func(outputs, labels)  
            accuracy(outputs, labels, correct_sum, topk=TOPK)
            total += labels.size(0)
            val_loss += loss.data.item()
            num_batches += 1 
        print('validation loss: ', val_loss/num_batches)
        print("validation accuracy: ", [ci/total for ci in correct_sum])
        return [ci/total for ci in correct_sum]

