        model_dir = self.save_dir + str(model_name) + self.model_ext
        self.saver.restore(sess, model_dir)
        print("Model restored from {}".format(model_dir))


def shuffle_tensors(x, y):
    assert len(x) == len(y), "Lengths don't match"
    if type(x) == list or type(y) == list:
        x = np.array(x)
        y = np.array(y)

    perm = np.random.permutation(len(x))
    return x[perm], y[perm]

def next_minibatch(x, y, minibatch_size):
    assert x.shape[0] == y.shape[0], "Shapes don't match"
    for i in range(0, x.shape[0] - minibatch_size + 1, minibatch_size):
        slice_range = slice(i, i + minibatch_size)
        yield x[slice_range], y[slice_range]
