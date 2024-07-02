import pickle

import torch
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from torch.utils.data.dataset import Dataset


class ECGDataset (Dataset):
