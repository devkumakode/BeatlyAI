    if not (counter % batch_size):
        X_train.append(inter_X_train)
        y_train.append(inter_y_train)
        inter_X_train = []
        inter_y_train = []

