    return np.array(labels)

def get_datasets(diseases, nr_inputs):
    datasets = []
    for disease in diseases:
        with open('datasets/processed/{}.csv'.format(disease)) as dis:
            dataset = np.loadtxt(dis)
            datasets.append(dataset)

    for idx, dataset in enumerate(datasets):
        _cutoff_val = reduce_ds(len(dataset), nr_inputs)
        _dataset = dataset[:_cutoff_val]
        datasets[idx] = _dataset.reshape(-1, nr_inputs)
        
    return datasets

def check_processed_dir_existance():
    if not os.listdir('datasets/processed'):
        print("You have to first process the data, " +
              "please call the download_data script")
