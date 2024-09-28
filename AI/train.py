        'optimizer_b_state_dict': optimizer_b.state_dict(),
        'parameters_w_bin': parameters_w_bin,
        }, file_name)


def save_model_ori(file_name, net, optimizer):
    """Save the state dictionary of model and optimizer for full precision training."""
    print('saving...')   
    torch.save({
        'net_state_dict': net.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        }, file_name)
def save_model_simple(file_name, net):
    """Save the state dictionary of model and optimizer for final training."""
    print('saving...')   
    torch.save({
        'net_state_dict': net.state_dict(),
        #'optimizer_state_dict': optimizer.state_dict(),
        }, file_name)
  
