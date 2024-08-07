            plt.plot(np.arange(start, end), y[start:end] - bias, cmap[int(y[i])])


def caculate_error(label_tuple, predict_tuple):
    error = np.zeros((5,))
    for i, (x, x_p) in enumerate(zip(label_tuple, predict_tuple)):
        error[i] = (x - x_p)/250*100  # (ms)
