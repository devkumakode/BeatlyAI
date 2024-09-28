        return self.x_train[index], self.y_train[index]  # 返回对应样本即可

    def __len__(self):
        return self.len


class TestDataset(Dataset):
    def __init__(self):
        base_path = './'
        dataset_path = './Dataset'
        classes = ['NSR', 'APB', 'AFL', 'AFIB', 'SVTA', 'WPW', 'PVC', 'Bigeminy',
                   'Trigeminy', 'VT', 'IVR', 'VFL', 'Fusion', 'LBBBB', 'RBBBB', 'SDHB', 'PR']
        ClassesNum = len(classes)
        X = list()
        y = list()

        for root, dirs, files in os.walk(dataset_path, topdown=False):
