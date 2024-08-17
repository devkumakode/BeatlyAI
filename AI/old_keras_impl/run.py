    inter_X_train.append(np.asarray(arrhy_data[i:i+500]))
    inter_y_train.append(0)
    inter_X_train.append(np.asarray(malignant_data[i:i+500]))
    inter_y_train.append(1)
    i += 500

validation_size = int(0.1  * len(X_train))

# remove the bugged batch
X_train.pop(0)
y_train.pop(0)

# split training and testing sets
X_train, X_test = np.split(X_train, [len(X_train)-validation_size])
