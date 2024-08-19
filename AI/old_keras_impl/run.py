y_train, y_test = np.split(y_train, [len(y_train)-validation_size])

# checking batch lengths
for batch in X_train:
    if len(batch) != 16:
        print("uneven batch with len: {}".format(len(batch)))
    for example in batch:
        if len(example) != 500:
            print("uneven example with len: {}".format(len(example)))


# shape = (X_train.shape[0], 16, 500)
shape = X_train.shape[1:]

