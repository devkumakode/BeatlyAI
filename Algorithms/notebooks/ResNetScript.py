

class ECGDataSet(Dataset):
    
    def __init__(self, split='train'):

        self.split = split

        # data loading
        current_directory = os.getcwd()
        self.parent_directory = os.path.dirname(current_directory)
