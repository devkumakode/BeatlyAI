    print('currrent binary filter number per layer: ')
    for p_w_bin in parameters_w_bin:
        print(p_w_bin.num_bin_filter)
    print('currrent average bitwidth per layer: ')
    for p_w_bin in parameters_w_bin:
        num_weight_layer += p_w_bin.num_weight
        num_bit_layer += p_w_bin.avg_bit*p_w_bin.num_weight
        print(p_w_bin.avg_bit)
        print(p_w_bin.num_weight)
    print('currrent average bitwidth: ', num_bit_layer/num_weight_layer)
    return parameters_w, parameters_b, parameters_w_bin 
      
     
def validate(net, val_loader, loss_func):
    """Get the validation loss and validation accuracy."""
    net.eval()
    val_loss = 0.
    num_batches = 0
    correct_sum = [0. for i in range(len(TOPK))]
