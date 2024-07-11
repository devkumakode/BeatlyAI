def get_data_loaders(config: DatasetConfig):
    return {
        Mode.train: data.DataLoader(
            EcgLoader(config.path[Mode.train], config.transforms[Mode.train]),
