import multiprocessing as mp
import os.path as osp
import subprocess
from glob import glob

from tqdm import tqdm

input_dir = "../mit-bih/*.atr"
ecg_data = sorted([osp.splitext(i)[0] for i in glob(input_dir)])
pbar = tqdm(total=len(ecg_data))


def run(file):
    params = ["python3", "dataset-generation.py", "--file", file]
    subprocess.check_call(params)
