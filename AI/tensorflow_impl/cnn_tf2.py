import time
import argparse

import tensorflow as tf
import numpy as np

from tensorflow.keras.layers import Dense, Flatten, Conv1D, BatchNormalization, MaxPool1D, Dropout
from tensorflow.keras.metrics import CategoricalAccuracy

from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, confusion_matrix
