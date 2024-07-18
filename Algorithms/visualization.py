    :param max_plots: max number of plots to show (in case of very long ecg)
    :return:
    """
    if end_offest is None:
        end_offest = ecg.shape[1]
    y_formatter = FixedFormatter(["none", "P wave", "QRS", "T wave", "Extra\nsystole"])
    y_locator = FixedLocator([0, 1, 2, 3, 4])

    for i, start in enumerate(range(start_offset, end_offest, plot_window)):
        fig, ax1 = plt.subplots(figsize=(20, 3))
