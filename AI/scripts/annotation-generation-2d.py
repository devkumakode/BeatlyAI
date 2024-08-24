
    val = data.loc[val_ids, :]
    train = data[~data.index.isin(val.index)]

    train.to_json(osp.join(output_path, "train.json"), orient="records")
    val.to_json(osp.join(output_path, "val.json"), orient="records")

    d = {}
    for label in train.label.unique():
        d[label] = len(d)

    with open(osp.join(output_path, "class-mapper.json"), "w") as file:
