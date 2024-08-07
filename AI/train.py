    train_loss = 0.
    num_batches = 0
    correct_sum = [0. for i in range(len(TOPK))]
    total = 0
    for (inputs, labels) in train_loader:               
        inputs, labels = inputs.cuda(non_blocking=True), labels.cuda(non_blocking=True)
        optimizer.zero_grad()    
        outputs = net(inputs)
        loss = loss_func(outputs, labels)
        loss.backward()   
        optimizer.step()
        accuracy(outputs, labels, correct_sum, topk=TOPK)
