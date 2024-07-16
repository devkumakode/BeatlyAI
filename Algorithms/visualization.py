import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter
from typing import Dict


def load_single_ecg(path: str) -> Dict[str, dict]:
    """annot format:
    {'data': {
        '<lead_name>': {
            'ecg': [[]],
            'label': [[]],
            'fs': int} },
     'legend': {0: 'none', 1: "p_wave", 2: "qrs", 3: "t_wave", 4: "extrasystole"}"""
    with open(path) as f:
        annot = json.load(f)
    return annot

