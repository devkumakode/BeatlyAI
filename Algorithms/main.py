    ecg_val_db = ECGDataset(data_path=config.RESOURCES_DIR + val_data_path, transform=normalizer_val)
    val_loader = DataLoader(
            ecg_val_db,
            batch_size=BATCH_SIZE,
            shuffle=True,
