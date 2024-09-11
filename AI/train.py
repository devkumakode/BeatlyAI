        accuracy(outputs, labels, correct_sum, topk=TOPK)
        train_loss += loss.data.item()
        num_batches += 1
        total += labels.size(0)
    print("epoch: ", epoch, ", pruning loss: ", train_loss/num_batches)                
    print('pruning accuracy: ', [ci/total for ci in correct_sum])
    num_weight_layer = 0.
    num_bit_layer = 0.
    print('currrent number of binary filters per layer: ')
    for p_w_bin in parameters_w_bin:
        print(p_w_bin.num_bin_filter)
    print('currrent average bitwidth per layer: ')
    for p_w_bin in parameters_w_bin:
        num_weight_layer += p_w_bin.num_weight
        num_bit_layer += p_w_bin.avg_bit*p_w_bin.num_weight
        print(p_w_bin.avg_bit)
