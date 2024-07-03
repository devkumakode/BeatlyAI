import pickle

import numpy as np
import torch
from sklearn.metrics import classification_report
from sklearn.metrics._plot import confusion_matrix

import config
from util.utils import plot_learning_curve
from util.utils import plot_confusion_matrix
from visualization import visualise_ecg


# def eval(val_loader, model, criterion, params, epoch, logger):
# 	"""Main method to evaluate model."""
# 	model.eval()
# 	print("================================")
# 	print("Evaluating...")
#
# 	loss = 0
