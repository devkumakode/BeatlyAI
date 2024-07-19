    fitted_min_max_scaler_test = fit_min_max_scaler(path=config.RESOURCES_DIR + test_data_path)

    normalizer_train = PyTorchMinMaxScalerVectorized(fitted_min_max_scaler_train)
    normalizer_val = PyTorchMinMaxScalerVectorized(fitted_min_max_scaler_val)
    normalizer_test = PyTorchMinMaxScalerVectorized(fitted_min_max_scaler_test)

    # loading data
    ecg_train_db = ECGDataset(data_path=config.RESOURCES_DIR + train_data_path, transform=normalizer_train)

