
def visualise_ecg(ecg: np.ndarray,
                  labels: np.ndarray,
                  pred_vec: np.ndarray = None,
                  start_offset: int = 0,
                  end_offest: int = None,
                  plot_window: int = 300,
                  max_plots: int = 2) -> None:
    """

    :param ecg: ecg signal
    :param labels: array of the same length as ecg, containing labels [0, 1, 2, 3, 4]
    :param pred_vec: same sa labels, but it is expected to be the model predictions
    :param start_offset: plot from given time-step (array index)
    :param end_offest: plot until given time-step (array index)
    :param plot_window: width of the plot window (array index units)
