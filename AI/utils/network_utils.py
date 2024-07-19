import torch


def load_checkpoint(path, model, optimizer=None):
    pth = torch.load(path)
