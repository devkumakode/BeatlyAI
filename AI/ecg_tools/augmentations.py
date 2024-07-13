class RandomShift:

    def __init__(self, max_num_samples: int, probability=0.5) -> None:
        self._m = max_num_samples
        self._p = probability

    def __call__(self, signal):
        if torch.rand(1) > self._p:
            return signal

