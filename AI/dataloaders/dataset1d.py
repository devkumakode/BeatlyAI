import json

import numpy as np
import wfdb
from scipy.signal import find_peaks
from sklearn.preprocessing import scale
from torch.utils.data import DataLoader, Dataset


class EcgDataset1D(Dataset):
    def __init__(self, ann_path, mapping_path):
        super().__init__()
        self.data = json.load(open(ann_path))
