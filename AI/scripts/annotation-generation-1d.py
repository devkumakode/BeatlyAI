    files = glob(data_path)

    for file in glob(data_path):
        *_, name, lead, label, filename = file.split("/")
        dataset.append(
            {
                "name": name,
                "lead": lead,
                "label": label,
                "filename": osp.splitext(filename)[0],
                "path": file,
            },
        )

    data = pd.DataFrame(dataset)
    data = data[data["lead"] == lead]
