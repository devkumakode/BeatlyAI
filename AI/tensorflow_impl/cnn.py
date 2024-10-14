    print("-"*50)

    # Total training time
    print("Total training time: {0:.2f}s".format(time.time() - total_time))
    loss, acc = sess.run([cost, accuracy], feed_dict={x: X_train,
                                                      y: Y_train,
                                                      keep_prob: 1.0})
    
   
    print("Training Accuracy: {0:.4f}".format(acc))
    print("Training Loss: {0:.4f}".format(loss))
