import torch
from tqdm import tqdm

from ecg_tools.config import EcgConfig, Mode
from ecg_tools.data_loader import get_data_loaders
from ecg_tools.metrics import Metrics
from ecg_tools.model import ECGformer


class ECGClassifierTrainer:

    def __init__(self, config: EcgConfig) -> None:
        self.model = ECGformer(
            embed_size=config.model.embed_size,
            num_layers=config.model.num_layers,
            num_heads=config.model.num_heads,
            num_classes=config.model.num_classes,
