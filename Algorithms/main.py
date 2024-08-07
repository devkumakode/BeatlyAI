        eval(
            ecgs=ecgs,
            y_true=y_true,
            y_pred=y_pred,
            labels=[0, 1, 2, 3, 4],
            target_names=['none', 'p_wave', 'qrs', 't_wave', 'extrasystole'],
            plot_acc=True,
            plot_loss=True,
            plot_conf_matrix=True,
            plot_ecg=True,
            plot_ecg_windows_size=WINDOWS_SIZE
        )




