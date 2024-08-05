    name = osp.basename(ecg)
    record = rdrecord(ecg)
    ann = wfdb.rdann(ecg, extension="atr")
    for sig_name, signal in zip(record.sig_name, record.p_signal.T):
        if not np.all(np.isfinite(signal)):
            continue
