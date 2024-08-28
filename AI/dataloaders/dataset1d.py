            raise Exception("No MLII LEAD")

        self.peaks = find_peaks(self.signal, distance=180)[0]
        mask_left = (self.peaks - self.mode // 2) > 0
        mask_right = (self.peaks + self.mode // 2) < len(self.signal)
        mask = mask_left & mask_right
        self.peaks = self.peaks[mask]

    def __getitem__(self, index):
        peak = self.peaks[index]
        left, right = peak - self.mode // 2, peak + self.mode // 2

        img = self.signal[left:right]
