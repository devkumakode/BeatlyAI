import dataclasses
from enum import Enum
from typing import Dict, Union

from ecg_tools.augmentations import Compose, RandomNoise, RandomShift


class Mode(Enum):
    train = "train"
    eval = "eval"


@dataclasses.dataclass()
class DatasetConfig:
    batch_size: int = 64
    num_workers: int = 8
    path: Dict = dataclasses.field(default_factory=lambda: {
