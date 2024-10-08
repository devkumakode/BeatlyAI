        checkpoint = torch.load(args.model_ori)
        net.load_state_dict(checkpoint['net_state_dict'])
        for name, param in net.named_parameters():
            print(name)
            print(param.size())
        print('initialization (structured sketching)...')
        parameters_w, parameters_b, parameters_w_bin = initialize(
            net, train_loader, loss_func, args.structure, args.subc, args.max_bit)
        optimizer_b = torch.optim.Adam(parameters_b, weight_decay=args.wd)
        optimizer_w = ALQ_optimizer(parameters_w, weight_decay=args.wd)
        val_accuracy = validate(net, val_loader, loss_func)
        best_acc = val_accuracy[0]
        test(net, test_loader, loss_func)
        save_model(args.model, net, optimizer_w, optimizer_b, parameters_w_bin)
        # print(parameters_w)
        # save_model_simple('./ALQ_in.pt',net)
        num_training_sample = len(train_dataset)
        M_p = (args.pr/args.top_k)/(args.epoch_prune *
                                    math.ceil(num_training_sample/args.batch_size))

        for r in range(args.R):

            print('outer iteration: ', r)
            optimizer_b.param_groups[0]['lr'] = args.lr
            optimizer_w.param_groups[0]['lr'] = args.lr

            print('optimizing basis...')
            for q_epoch in range(args.epoch_basis):
                optimizer_b.param_groups[0]['lr'] *= args.ld_basis
                optimizer_w.param_groups[0]['lr'] *= args.ld_basis
                train_basis(net, train_loader, loss_func, optimizer_w,
                            optimizer_b, parameters_w_bin, q_epoch)
                val_accuracy = validate(net, val_loader, loss_func)
                if val_accuracy[0] > best_acc:
                    best_acc = val_accuracy[0]
                    test(net, test_loader, loss_func)
                    #save_model(args.model, net, optimizer_w, optimizer_b, parameters_w_bin)

            print('optimizing coordinates...')
            for p_epoch in range(args.epoch_coord):
                optimizer_b.param_groups[0]['lr'] *= args.ld_coord
                optimizer_w.param_groups[0]['lr'] *= args.ld_coord
                train_coordinate(net, train_loader, loss_func,
                                 optimizer_w, optimizer_b, parameters_w_bin, p_epoch)
                val_accuracy = validate(net, val_loader, loss_func)
                if val_accuracy[0] > best_acc:
                    best_acc = val_accuracy[0]
                    test(net, test_loader, loss_func)
                    #save_model(args.model, net, optimizer_w, optimizer_b, parameters_w_bin)

            print('pruning...')
            for t_epoch in range(args.epoch_prune):
                prune(net, train_loader, loss_func, optimizer_w,
                      optimizer_b, parameters_w_bin, [args.top_k, M_p], t_epoch)
                val_accuracy = validate(net, val_loader, loss_func)
                best_acc = val_accuracy[0]
                test(net, test_loader, loss_func)
                save_model(args.model, net, optimizer_w,
                           optimizer_b, parameters_w_bin)
        save_model_simple('./ECGNet_model_q_afterALQ.pt', net)
        print(net.features[0].weight)
        print(net.features[3].weight)
        print(net.features[6].weight)
        print(net.features[9].weight)
        print(net.features[12].weight)
        print(net.features[15].weight)
        print(net.features[18].weight)
        print(net.classifier[0].weight)
        print(net.classifier[3].weight)
        torch.save(net, 'a.pth')
    if args.POSTTRAIN:
        print('posttraining...')

