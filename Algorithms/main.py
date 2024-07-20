            num_workers=0
    )

    ecg_test_db = ECGDataset(data_path=config.RESOURCES_DIR + test_data_path, transform=normalizer_test)
    test_loader = DataLoader(
            ecg_test_db,
            batch_size=BATCH_SIZE,
            shuffle=True,
            num_workers=0
    )

    if TRAIN:
        if CONTINUE_TRAIN:
            # continue training
            net = restore_net(save_path + '/epoch_35.ckpt')
            net.to(DEVICE)
        else:
            # model
            model_name = 'seg-net'
