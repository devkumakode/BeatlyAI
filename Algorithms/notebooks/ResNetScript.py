        train_small_path = os.path.join(self.parent_directory, 'data', 'deepfake-ecg-small', str(self.split) + '.csv')
        self.df = pd.read_csv(train_small_path)  # Skip the header row
        
        # Avg RR interval
        # in milli seconds
        RR = torch.tensor(self.df['avgrrinterval'].values, dtype=torch.float32)
