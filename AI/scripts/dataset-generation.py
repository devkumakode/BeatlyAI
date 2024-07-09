import argparse
import os
import os.path as osp

import cv2
import matplotlib.pyplot as plt
import numpy as np
import wfdb
from sklearn.preprocessing import scale
from wfdb import rdrecord

# Choose from peak to peak or centered
# mode = [20, 20]
mode = 128

image_size = 128
output_dir = "../data"

