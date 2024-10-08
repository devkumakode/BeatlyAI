    y_pred = np.argmax(y_pred, axis=1)
    y_true = np.argmax(Y_test, axis=1)

    # Precision and recall could also be done as callbacks in the evaluate or fit function
    print("Precision: {}".format(precision_score(y_true, y_pred, average='micro')))
    print("Recall: {}".format(recall_score(y_true, y_pred, average='micro')))
    print("Confusion matrix: \n{}".format(confusion_matrix(y_true, y_pred, labels=[0,1,2])))
