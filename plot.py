from data import read_data
import matplotlib.pyplot as plt
import numpy as np

def plot_counts(ax, title, counts, bottom=False):
    ax.set_title(title)
    if bottom:
        ax.set_xlabel('Counts per minute')
    ax.set_ylabel('Frequency')
    ax.get_yaxis().set_label_coords(-0.09, 0.5)
    ax.hist(counts, bins=range(2, 40))# 32))

def plot():
    data = read_data()
    medians = np.asarray([np.median(d['counts']) for d in data])

    fig, axes = plt.subplots(len(data), figsize=(5, 12))
    for i, data_id in enumerate(np.argsort(medians)):
        ax = axes[i]
        d = data[data_id]
        plot_counts(ax,
                    d['location_human_readable'],
                    d['counts'],
                    bottom=i==len(data)-1)

    plt.tight_layout()
    plt.savefig('plot.png', dpi=200)
    plt.show()
    return

    n = len(data)
    fig, axes = plt.subplots(n, figsize=(5, 10))
    for i, (ax, d) in enumerate(zip(axes, data)):
        plot_counts(ax,
                    d['location_human_readable'],
                    d['counts'],
                    bottom=i==n-1)
    # plt.subplots_adjust(hspace=1)
    plt.tight_layout()
    plt.savefig('plot.png', dpi=200)
    plt.show()
