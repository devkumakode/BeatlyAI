import os
import os.path as osp
from datetime import datetime

import numpy as np
import torch
from tqdm import tqdm

from utils.network_utils import load_checkpoint


class BaseRunner:
    def __init__(self, config):
        self.config = config
        self.exp_name = self.config.get("exp_name", None)
        if self.exp_name is None:
            self.exp_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.res_dir = osp.join(self.config["exp_dir"], self.exp_name, "results")
        os.makedirs(self.res_dir, exist_ok=True)
