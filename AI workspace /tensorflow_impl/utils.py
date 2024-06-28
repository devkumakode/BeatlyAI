def reduce_ds(dataset_len, nr_inputs):
    # fit the dataset length to the number of input neurons
    return dataset_len - (dataset_len % nr_inputs)

