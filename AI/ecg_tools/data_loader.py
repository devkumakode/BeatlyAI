            batch_size=config.batch_size,
            num_workers=config.num_workers,
            shuffle=True
        ),
        Mode.eval: data.DataLoader(
            EcgLoader(config.path[Mode.eval], config.transforms[Mode.eval]),
            batch_size=config.batch_size,
            num_workers=config.num_workers,
            shuffle=False
        )
    }


if __name__ == "__main__":
    loader = get_data_loaders(DatasetConfig())
