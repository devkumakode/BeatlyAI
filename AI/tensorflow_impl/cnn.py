
# Initializing the variables
init = tf.global_variables_initializer()

X_train, X_test, Y_train, Y_test = model.get_data()


# Launch the graph
with tf.Session() as sess:
    # Initialize the variables for the current session
    sess.run(init)

    # Add the graph to tensorboard writer
    model.tensorboard_handler.writer.add_graph(sess.graph)
    step = 1

    # If restore_model flag True, restore the model
    if restore_model:
        model.saver.restore(sess)

    # Set start time
    total_time = time.time()
    epoch_time = time.time()

    print("-"*50)
    # Train
    for epoch in range(1, epochs):
        for X_train_batch, Y_train_batch in next_minibatch(X_train, Y_train, batch_size):
            sess.run(optimizer, feed_dict={x: X_train_batch,
                                           y: Y_train_batch,
                                           keep_prob: dropout})

            # Once a few steps run the accuracy for the training model
            if verbose and (step % display_step) == 0:
                loss, acc = sess.run([cost, accuracy],
                                     feed_dict={x: X_train,
                                                y: Y_train,
                                                keep_prob: 1.0})

                print("Step: {}".format(step))
                print("Training loss: {:.4f}".format(loss))
                print("Training Accuracy: {:.4f}".format(acc))

            step += 1

