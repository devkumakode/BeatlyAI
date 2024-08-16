        outputs = net(inputs)
        loss = loss_func(outputs, labels)
        loss.backward()   
        optimizer_b.step()
        optimizer_w.step(parameters_w_bin, 'coordinate')
        accuracy(outputs, labels, correct_sum, topk=TOPK)
        total += labels.size(0)
        train_loss += loss.data.item()
        num_batches += 1    
