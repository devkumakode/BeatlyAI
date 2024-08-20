    dataset_dir = "datasets/raws"
    
    def check_folder_existance():
        if not os.path.isdir(dataset_dir):
            print("Directory {} not found".format(dataset_dir))
            print("Creating now...")
            os.makedirs(dataset_dir)

        for database in physionet:
            folder = os.path.join(dataset_dir, database)
            if not os.path.isdir(folder):
                print("Directory {} not found".format(folder))
                print("Creating now...")
                os.makedirs(folder)

    def rdsamp_installed():
        try:
            subprocess.call(["rdsamp", "-h"], stdout=subprocess.DEVNULL,
                                              stderr=subprocess.DEVNULL)
            return True
