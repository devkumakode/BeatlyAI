dropout = args.dropout
restore_model = args.restore_model
freeze = args.freeze
heart_diseases = args.heart_diseases
verbose = args.verbose

# Network Parameters
nr_inputs = 350 # changing this will also have to change the shape from wdense1
nr_classes = len(heart_diseases)

# TF Graph input
