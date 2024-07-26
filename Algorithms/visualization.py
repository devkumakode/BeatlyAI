
        ax2 = ax1.twinx()
        if pred_vec is not None:
            ax2.plot(pred_vec[start:start + plot_window], '.', color='red')
        ax2.plot(labels[0, start:start + plot_window] + 0.1, '.', color='green')
        ax2.set_ylim(ymin=-0.1, ymax=4.3)
        ax2.yaxis.set_major_formatter(y_formatter)
        ax2.yaxis.set_major_locator(y_locator)
        if i >= max_plots - 1:
            print("max_plots was reached, increase it to see more")
            break
    plt.show()

