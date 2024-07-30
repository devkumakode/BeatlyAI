
import tensorflow as tf
import numpy as np


class TensorBoardHandler(object):
    def __init__(self, logs_path=None):
        self.logs_path = logs_path if logs_path else "tensorboard_data/others/"
        self.writer = tf.summary.FileWriter(self.logs_path)

    def add_histograms(self, dct):
        for k, v in dct.items():
            tf.summary.histogram(str(k), v)

    def add_scalar(self, name, obj):
        return tf.summary.scalar(name, obj)

    def merge_all(self):
        return tf.summary.merge_all()
