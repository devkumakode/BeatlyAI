        

def save_model(file_name, net, optimizer_w, optimizer_b, parameters_w_bin):
    """Save the state dictionary of model and optimizers."""
    print('saving...')   
    torch.save({
        'net_state_dict': net.state_dict(),
        'optimizer_w_state_dict': optimizer_w.state_dict(),
