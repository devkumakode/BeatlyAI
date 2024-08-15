par.add_argument("-e", dest="epochs",
                 type=int, default=50,
                 help="The number of epochs the model will train for")

par.add_argument("-bs", dest="batch_size",
                 type=int, default=32,
                 help="The batch size of the model")

