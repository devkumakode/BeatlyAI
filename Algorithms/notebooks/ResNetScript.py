        self.samples = self.df.shape[0]

    def __getitem__(self, index):
        
        # file path
        filename= self.df['patid'].values[index]
        asc_path = os.path.join(self.parent_directory, 'data', 'deepfake-ecg-small', str(self.split), str(filename) + '.asc')
        
