    train_loader = DataLoader(
            ecg_train_db,
            batch_size=BATCH_SIZE,
            shuffle=True,
            num_workers=0
    )

