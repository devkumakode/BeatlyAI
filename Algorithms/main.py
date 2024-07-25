            net = model_factory(model_name)
            net.to(DEVICE)

        optimizer = torch.optim.Adam(net.parameters(), lr=1e-3)
        criterion = nn.CrossEntropyLoss()
        optimizer.zero_grad()

        train(
                train_loader=train_loader,
                val_loader=val_loader,
