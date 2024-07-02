import argparse
import os
import scipy.io as scio
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import torch.optim as optim
import math
from torchvision import datasets, transforms
import numpy as np
from binarynet import ConvLayer_bin, FCLayer_bin
from myoptimizer import ALQ_optimizer
from train import get_accuracy, train_fullprecision, train_basis, train_basis_STE, train_coordinate, validate, test, prune, initialize, save_model, save_model_ori, save_model_simple

# Defining the network (ECGNet5)
in_channels_ = 1
