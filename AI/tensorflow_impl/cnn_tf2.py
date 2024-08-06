
from utils import get_labels, get_datasets, check_processed_dir_existance


par = argparse.ArgumentParser(description="ECG Convolutional " +
                                           "Neural Network implementation with Tensorflow 2.0")

par.add_argument("-lr", dest="learning_rate",
                 type=float, default=0.001,
                 help="Learning rate used by the model")

