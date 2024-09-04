        x = self.features(x)
        x = x.view((-1, 216))
        x = self.classifier(x)
        return x


class MyDataset(Dataset):
    def __init__(self):
        base_path = './'
        dataset_path = './Dataset'
        classes = ['NSR', 'APB', 'AFL', 'AFIB', 'SVTA', 'WPW', 'PVC', 'Bigeminy',
                   'Trigeminy', 'VT', 'IVR', 'VFL', 'Fusion', 'LBBBB', 'RBBBB', 'SDHB', 'PR']
