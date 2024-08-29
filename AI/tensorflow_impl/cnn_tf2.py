par.add_argument("--dropout", type=float, default=0.5,
                 help="Dropout probability")

par.add_argument("--restore", dest="restore_model",
                 action="store_true", default=False,
                 help="Restore the model previously saved")

par.add_argument("--freeze", dest="freeze",
                 action="store_true", default=False,
                 help="Freezes the model")

par.add_argument("--heart-diseases", nargs="+",
