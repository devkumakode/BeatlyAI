        self.save_dir = save_dir if save_dir else "saved_models/others/"

        # Create directory to store models
        if not os.path.isdir(self.save_dir):
            print("Saved model dir not found")
            print("Creating {}".format(self.save_dir))
            os.makedirs(self.save_dir)
        self.saver = tf.train.Saver(*args, **kwargs)

    def save(self, sess, model_name="model"):
        model_dir = self.save_dir + str(model_name) + self.model_ext
        self.saver.save(sess, model_dir)
        print("Model saved to {}".format(model_dir))
        
    def restore(self, sess, model_name="model"):
