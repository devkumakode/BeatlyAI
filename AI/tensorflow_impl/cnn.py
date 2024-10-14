
    # If model not freezed, save the model
    if not freeze:
        model.saver.save(sess)

    # Run testing accuracy
    acc = sess.run(accuracy, feed_dict={x: X_test,
                                        y: Y_test,
                                        keep_prob: 1.0})
    print("Testing Accuracy: {0:.4f}".format(acc))
    print("-"*50)

