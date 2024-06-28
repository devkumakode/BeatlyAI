if __name__ == '__main__':
    data_root = 'resources/ecg-data'
    ecg_id = 232  # choose ecg id from [0, 289]

    # load split file containing paths to the data
    df = pd.read_csv(os.path.join(data_root, 'split.csv'))

    path = df.iloc[ecg_id]['name']
    lead_name = path.split('/')[1][:-5]  # extract lead name
    annot = load_single_ecg(os.path.join(data_root, path))

    ecg = np.array(annot['data'][lead_name]['ecg'])  # ecg signal as numpy array (for visualisation)
    label = np.array(annot['data'][lead_name]['label'])
    visualise_ecg(ecg, label, plot_window=5000)
    print("done")

