

par = argparse.ArgumentParser(description="ECG Convolutional " +
                                           "Neural Network implementation")

par.add_argument("-lr", dest="learning_rate",
                 type=float, default=0.001,
                 help="Learning rate used by the model")
