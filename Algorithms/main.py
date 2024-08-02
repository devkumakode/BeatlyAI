        net = restore_net(PATH_TO_TEST_MODEL)
        net.eval()
        net.to(DEVICE)

        # after the training run function for train/val/test loader
        loader = test_loader

        ecgs, y_true, y_pred = test(
                net=net,
                test_loader=loader,
                device=DEVICE,
                batch_size=BATCH_SIZE,
                plot_ecg=False,
                plot_ecg_windows_size=WINDOWS_SIZE
        )

