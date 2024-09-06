        val_ids.extend(
            data[data["label"] == cl]
            .sample(frac=val_size, random_state=random_state)
            .index,
