
# Define loss and optimizer
cost = model.cost(pred)

# Add scalar summary to cost tensor
model.tensorboard_handler.add_scalar("training_loss", cost)

# Create optimier
optimizer = model.optimizer(cost)

# Evaluate model
accuracy = model.evl(pred)

# Add scalar summary to accuracy tensor
