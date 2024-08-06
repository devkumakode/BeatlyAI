from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from ecg_tools.config import Mode


class Metrics:

    def __init__(self) -> None:
        self.predictions = []
        self.labels = []

    def reset(self):
        self.predictions = []
