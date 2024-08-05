
    for file in glob(data_path):
        *_, name, lead, label, filename = file.split("/")
        dataset.append(
            {
