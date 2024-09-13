    print('currrent average bitwidth: ', num_bit_layer/num_weight_layer)

 
def initialize(net, train_loader, loss_func, structure, num_subchannel, max_bit):
    """Initialize the weight tensors of all layers to multi-bit form using structured sketching. 
    Return the iterator over all weight parameters, the iterator over all other parameters, and the iterator over the multi-bit forms of all weight parameters.  
    """
    parameters_w = []
    parameters_b = []
    parameters_w_bin = []
    i = 0
    for name, param in net.named_parameters():
        # Only initialize weight tensors to multi-bit form
