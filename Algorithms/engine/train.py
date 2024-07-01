import matplotlib.pyplot as plt
import numpy as np
import torch

import config
from util import save_as_pkl


def plotecg(x, y, start, end):
    x = x[start:end, 0]
    y = y[start:end]
