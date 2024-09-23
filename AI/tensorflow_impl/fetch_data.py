    for ecg_name in ecg_dirs:
        print("Processing {}".format(ecg_name))
        processed_csv = os.path.join(processed_dir, ecg_name) + ".csv"
        with open(processed_csv, 'w') as write_processed_file:
            csvwriter = csv.writer(write_processed_file, delimiter=',')
            record_dir = os.path.join(raw_dir, ecg_name)
            for record in os.listdir(record_dir):
                if record.endswith('.csv'):
                    record_path = os.path.join(record_dir, record)

                    with open(record_path) as read_raw_file:
                        reader = csv.reader(read_raw_file)
                        # skip headers
                        reader.__next__()
                        reader.__next__()
                        for row in reader:
                            csvwriter.writerow([row[1]])
    print("Done")


