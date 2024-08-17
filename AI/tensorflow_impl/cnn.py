        'bconv1': tf.Variable(tf.random_normal([64])),
        'bconv2': tf.Variable(tf.random_normal([128])),
        'bconv3': tf.Variable(tf.random_normal([128])),
        'bconv4': tf.Variable(tf.random_normal([256])),
        'bdense1': tf.Variable(tf.random_normal([1024])),
        'bdense2': tf.Variable(tf.random_normal([2048])),
        'bout': tf.Variable(tf.random_normal([nr_classes]))
    }

    def __init__(self, weights=None, biases=None):
        self.weights = weights if weights else self.weights
        self.biases = biases if biases else self.biases
        self.datasets = get_datasets(heart_diseases, nr_inputs)
        self.label_data = get_labels(self.datasets)

