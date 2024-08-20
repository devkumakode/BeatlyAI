        self.mode = mode
        for sig_name, signal in zip(record.sig_name, record.p_signal.T):
            if sig_name in ["MLII", "II"] and np.all(np.isfinite(signal)):
                self.signal = scale(signal).astype("float32")
        if self.signal is None:
