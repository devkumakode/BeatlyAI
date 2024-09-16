            subprocess.check_call(cmd, shell=True)
    print("Done")


def process_data():
    print("Processing data...")
    raw_dir = "datasets/raws"
    processed_dir = "datasets/processed"
    
    ecg_dirs = os.listdir(raw_dir)
    
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

