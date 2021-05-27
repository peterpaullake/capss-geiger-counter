import json
import matplotlib.pyplot as plt
import numpy as np

def read_data(path):
    return np.asarray([int(line) for line in open(path).readlines()])

def plot_data(ax, title, path, bottom=False):
    ax.set_title(title)
    if bottom:
        ax.set_xlabel('Counts per minute')
    ax.set_ylabel('Frequency')
    ax.get_yaxis().set_label_coords(-0.09, 0.5)
    ax.hist(read_data(path), bins=range(2, 32))

def plot():
    data = json.loads(open('json.json').read())
    n = len(data)
    fig, axes = plt.subplots(n)
    for i, (ax, d) in enumerate(zip(axes, data)):
        plot_data(ax,
                  d['location_human_readable'],
                  d['path'],
                  bottom=i==n-1)
    plt.subplots_adjust(hspace=0.5)
    plt.tight_layout()
    plt.savefig('plot.png', dpi=200)
    plt.show()
