
    print("-"*50)

    # Total training time
    print("Total training time: {0:.2f}s".format(time.time() - total_time))

    # Test
    model.cnn_model.evaluate(X_test, Y_test, batch_size=batch_size)
    print("-"*50)
    print("Testing results:")
    y_pred = model.cnn_model.predict(X_test, batch_size=batch_size)

    # The following scikit-learn methods only accept array of labels, not one hot encodings
