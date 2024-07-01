from typing import Callable

import pandas as pd
import torch
import torch.utils.data as data

from ecg_tools.config import DatasetConfig, Mode


class EcgLoader(data.Dataset):

    def __init__(self, csv_file, transforms: Callable = lambda x: x) -> None:
        super().__init__()
        self.annotations = pd.read_csv(csv_file).values
