
model = KanResWide_X2(input_shape, output_size)
model.to(device)
print(model)

import torch.optim as optim

# Loss function for linear values (e.g., regression)
loss_fn = nn.MSELoss()  # Mean Squared Error loss

# Adam optimizer
optimizer = optim.Adam(model.parameters(), lr=1e-3)  # You can adjust lr and other hyperparameters

epochs = 50
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    #test(validate_dataloader, model, loss_fn)
