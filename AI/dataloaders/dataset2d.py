import json

import cv2
from albumentations import Compose, Normalize
from albumentations.pytorch.transforms import ToTensorV2
from torch.utils.data import DataLoader, Dataset

augment = Compose([Normalize(), ToTensorV2()])


class EcgDataset2D(Dataset):
    def __init__(self, ann_path, mapping_path):
        super().__init__()
        self.data = json.load(open(ann_path))
