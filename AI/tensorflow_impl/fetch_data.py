    if not rdsamp_installed():
        sys.exit(1)

    for database, samples in physionet.items():
        print("Downloading {}".format(database))
        database_dir = os.path.join(dataset_dir, database)
        for sample in samples:
            csv_file_path = os.path.join(database_dir, sample) + ".csv"
            if os.path.exists(csv_file_path):
                print("File {} exists. Skipping download...".format(csv_file_path))
                continue

            sample_path = os.path.join(database, sample)
            cmd = ("rdsamp -r {} -c -H -f 0" +
                   " -t 60 -v -pe > {}").format(sample_path, csv_file_path)
            try:
