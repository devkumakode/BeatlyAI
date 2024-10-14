        print("#"*50)
        print("Epoch summary:")
        print("Epoch: {}".format(epoch))
        print("Training took: {0:.2f}s".format(time.time() - epoch_time))
        summary, acc = sess.run([merged, accuracy],
                                feed_dict={x: X_train,
                                           y: Y_train,
                                           keep_prob: 1.0})
        print("Training accuracy: {0:.4f}".format(acc))

        # Run testing accuracy
        acc = sess.run(accuracy, feed_dict={x: X_test,
                                            y: Y_test,
                                            keep_prob: 1.0})
        print("Testing accuracy: {0:.4f}".format(acc))
        print("#"*50)

        # write to log
        model.tensorboard_handler.writer.add_summary(summary, epoch)

        # Reset epoch time
        epoch_time = time.time()

