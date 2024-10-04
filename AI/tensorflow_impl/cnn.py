model.tensorboard_handler.add_scalar("training_accuracy", accuracy)
# testing_acc = model.tensorboard_handler.add_scalar("testing_accuracy", accuracy)

# Merge tensorboard data
merged = model.tensorboard_handler.merge_all()
