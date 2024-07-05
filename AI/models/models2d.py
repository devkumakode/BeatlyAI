import torch.nn as nn
from efficientnet_pytorch import EfficientNet as efficientnet
from torchvision import models


class HeartNet(nn.Module):
    def __init__(self, num_classes=7):
        super(HeartNet, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.ELU(inplace=True),
            nn.BatchNorm2d(64, eps=0.001),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.ELU(inplace=True),
            nn.BatchNorm2d(64, eps=0.001),
            nn.MaxPool2d(kernel_size=2, stride=2),
