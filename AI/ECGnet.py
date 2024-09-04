        ClassesNum = len(classes)
        X = list()
        y = list()

        for root, dirs, files in os.walk(dataset_path, topdown=False):
            for name in files:
                data_train = scio.loadmat(
                    os.path.join(root, name))  # 取出字典里的value
