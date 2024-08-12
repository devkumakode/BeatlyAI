    def __len__(self):
        return len(self.data)


def callback_get_label(dataset, idx):
    return dataset[idx]["class"]


class EcgPipelineDataset1D(Dataset):
    def __init__(self, path, mode=128):
        super().__init__()
        record = wfdb.rdrecord(path)
        self.signal = None
