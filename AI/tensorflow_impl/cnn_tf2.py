                 dest="heart_diseases",
                 default=["apnea-ecg", "svdb", "afdb"],
                 choices=["apnea-ecg", "mitdb", "nsrdb", "svdb", "afdb"],
                 help="Select the ECG diseases for the model")

par.add_argument("--verbose", dest="verbose",
                 action="store_true", default=False,
                 help="Display information about minibatches")

args = par.parse_args()

# Parameters
learning_rate = args.learning_rate
epochs = args.epochs
batch_size = args.batch_size
display_step = args.display_step
dropout = args.dropout
