# dpi fix
fig = plt.figure(frameon=False)
dpi = fig.dpi

# fig size / image size
figsize = (image_size / dpi, image_size / dpi)
image_size = (image_size, image_size)


def plot(signal, filename):
    plt.figure(figsize=figsize, frameon=False)
    plt.axis("off")
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
