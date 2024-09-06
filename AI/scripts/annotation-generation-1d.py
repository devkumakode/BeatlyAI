    data = data[data["label"].isin(classes)]
    data = data.sample(frac=1, random_state=random_state)

    val_ids = []
    for cl in classes:
