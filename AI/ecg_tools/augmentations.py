import torch


class Compose:

    def __init__(self, transforms) -> None:
        self.transforms = transforms

    def __call__(self, signal):
        for t in self.transforms:
            signal = t(signal)
        return signal


