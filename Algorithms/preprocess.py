import json
import os
import pickle

import BaselineWanderRemoval
import numpy as np
import pandas as pd

import config

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)


INSPECT = False
WINDOW_LEN = 220
