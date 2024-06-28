            print(p_w_bin.avg_bit)
        print('currrent average bitwidth: ', num_bit_layer/num_weight_layer)

        get_accuracy(net, train_loader, loss_func)
        val_accuracy = validate(net, val_loader, loss_func)
        best_acc = val_accuracy[0]
        test(net, test_loader, loss_func)
        optimizer_b.param_groups[0]['lr'] = args.lr
        optimizer_w.param_groups[0]['lr'] = args.lr

        print('optimizing basis with STE...')
        for epoch in range(50):
            optimizer_b.param_groups[0]['lr'] *= 0.95
            optimizer_w.param_groups[0]['lr'] *= 0.95
            train_basis_STE(net, train_loader, loss_func,
                            optimizer_w, optimizer_b, parameters_w_bin, epoch)
            val_accuracy = validate(net, val_loader, loss_func)
            if val_accuracy[0] > best_acc:
                best_acc = val_accuracy[0]
                test(net, test_loader, loss_func)
                save_model(args.model, net, optimizer_w,
                           optimizer_b, parameters_w_bin)

        print('optimizing coordinates...')
        for epoch in range(20):
            optimizer_b.param_groups[0]['lr'] *= 0.9
            optimizer_w.param_groups[0]['lr'] *= 0.9
            train_coordinate(net, train_loader, loss_func,
                             optimizer_w, optimizer_b, parameters_w_bin, epoch)
            val_accuracy = validate(net, val_loader, loss_func)
            if val_accuracy[0] > best_acc:
                best_acc = val_accuracy[0]
                test(net, test_loader, loss_func)
                save_model(args.model, net, optimizer_w,
                           optimizer_b, parameters_w_bin)
        save_model_simple('./ECGNet_model_q.pth', net)
        torch.save(net, './test.pth')
