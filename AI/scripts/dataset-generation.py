        signal = scale(signal)
        for i, (label, peak) in enumerate(zip(ann.symbol, ann.sample)):
            if label == "/":
                label = "\\"
            print("\r{} [{}/{}]".format(sig_name, i + 1, len(ann.symbol)), end="")
            if isinstance(mode, list):
                if np.all([i > 0, i + 1 < len(ann.sample)]):
                    left = ann.sample[i - 1] + mode[0]
                    right = ann.sample[i + 1] - mode[1]
                else:
                    continue
            elif isinstance(mode, int):
                left, right = peak - mode // 2, peak + mode // 2
