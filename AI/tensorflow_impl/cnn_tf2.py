class CNN:
    def __init__(self):
        self.datasets = get_datasets(heart_diseases, n_inputs)
        self.label_data = get_labels(self.datasets)
        self.callbacks = []

        # Initialize callbacks
        tensorboard_logs_path = "tensorboard_data/cnn/"
        tb_callback = tf.keras.callbacks.TensorBoard(log_dir=tensorboard_logs_path,
                                                     histogram_freq=1, write_graph=True,
                                                     embeddings_freq=1)

        # load_weights_on_restart will read the filepath of the weights if it exists and it will
        # load the weights into the model
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath="saved_models/cnn/model.hdf5",
                                                         save_best_only=True,
                                                         save_weights_only=True,
                                                         load_weights_on_restart=restore_model)

        self.callbacks.extend([tb_callback, cp_callback])
