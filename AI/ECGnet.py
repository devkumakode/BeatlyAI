        net = ECGNet().cuda()
        loss_func = torch.nn.CrossEntropyLoss().cuda()

        parameters_w = []
        parameters_b = []
        for name, param in net.named_parameters():
            if 'weight' in name and param.dim() > 1:
                parameters_w.append(param)
            else:
                parameters_b.append(param)

        optimizer_b = torch.optim.Adam(parameters_b, weight_decay=args.wd)
        optimizer_w = ALQ_optimizer(parameters_w, weight_decay=args.wd)

        print('load quantized ECGNet model...')
        checkpoint = torch.load(args.model)
        net.load_state_dict(checkpoint['net_state_dict'])
        optimizer_w.load_state_dict(checkpoint['optimizer_w_state_dict'])
        optimizer_b.load_state_dict(checkpoint['optimizer_b_state_dict'])
        for state in optimizer_b.state.values():
            for k, v in state.items():
                if torch.is_tensor(v):
                    state[k] = v.cuda()
        for state in optimizer_w.state.values():
            for k, v in state.items():
                if torch.is_tensor(v):
                    state[k] = v.cuda()

        num_weight_layer = 0.
        num_bit_layer = 0.
        print('currrent binary filter number per layer: ')
        for p_w_bin in parameters_w_bin:
            print(p_w_bin.num_bin_filter)
        print('currrent average bitwidth per layer: ')
        for p_w_bin in parameters_w_bin:
            num_weight_layer += p_w_bin.num_weight
            num_bit_layer += p_w_bin.avg_bit*p_w_bin.num_weight
