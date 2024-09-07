        total += labels.size(0)
        train_loss += loss.data.item()
        num_batches += 1    
    print("epoch: ", epoch, ", training loss: ", train_loss/num_batches)                
    print('training accuracy: ', [ci/total for ci in correct_sum])


def prune(net, train_loader, loss_func, optimizer_w, optimizer_b, parameters_w_bin, pruning_rate, epoch):
