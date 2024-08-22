    data = data[data["lead"] == lead]
    data = data[data["label"].isin(classes)]
    data = data.sample(frac=1, random_state=random_state)

    val_ids = []
    for cl in classes:
        val_ids.extend(
            data[data["label"] == cl]
            .sample(frac=val_size, random_state=random_state)
            .index,
        )
