from keras.layers import Convolution1D
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, Dropout
from data import process_data
from keras import backend as K
import numpy  as np
import os

if not os.listdir('datasets/processed'):
    process_data()

arrhy_data = np.loadtxt(open('datasets/processed/arrhythmia.csv', 'r'), skiprows=1)
