def plotlabel(y, bias):
    cmap = ['k', 'r', 'g', 'b', 'c', 'y']
    start = end = 0
    for i in range(len(y) - 1):
        if y[i] != y[i + 1]:
            end = i
            plt.plot(np.arange(start, end), y[start:end] - bias, cmap[int(y[i])])
            start = i + 1
        if i == len(y) - 2:
            end = len(y) - 1
