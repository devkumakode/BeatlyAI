import torch
from torch import nn
from torch.utils.data import DataLoader

import config
from engine import test
from engine import train
from engine import eval
from modeling import ECGDataset, PyTorchMinMaxScalerVectorized, fit_min_max_scaler
from modeling import model_factory
from util import restore_net

TRAIN = False
CONTINUE_TRAIN = False
TEST = True
EPOCHS = 100
BATCH_SIZE = 32
NUM_SEGS_CLASS = 5
