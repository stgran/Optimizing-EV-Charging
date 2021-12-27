import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# def plot_bars(dataset, bars_col, labels_col, y_label, x_label, title, destination):
#     if labels_col == 'index':
#         labels = dataset.index
#     else:
#         labels = dataset[labels_col]
#     plt.bar(labels, dataset[bars_col], color=['#3F5589'])
#     plt.ylabel(y_label)
#     plt.xlabel(x_label)
#     plt.title(title)
#     plt.savefig(destination)
#     plt.clf()

# def subplot_bars(dataset, bars_cols, labels_col, y_label, x_label, title, destination):
#     fig, axs = plt.subplots(2, 4)
#     x = dataset[labels_col]
#     plot_number = 0
#     for col in range(4):
#         for row in range(2):
#             y = dataset[bars_cols[plot_number]]
#             axs[row, col].bar(x, y)
#             axs[row, col].set_title(bars_cols[plot_number])
#             plot_number += 1
#             for i, tick in enumerate(axs[row, col].xaxis.get_major_ticks()):
#                 if i % 4 != 0:
#                     tick.set_visible(False)

#     for i, ax in enumerate(axs.flat):
#         if i % 4 == 0:
#             ax.set(ylabel=y_label)
        
#         if i >= len(axs.flat) - 4:
#             ax.set(xlabel=x_label)
#         else:
#             ax.set_xticks([])
    
#     fig.set_size_inches(12, 8, forward=True)
    
#     fig.suptitle(title)

#     plt.savefig(destination)
#     plt.clf()

def seasonal_bars(dataset, bars_cols, labels_col, y_label, x_label, title, destination):
    fig, axs = plt.subplots(2, 2) # We want a 2x2 subplot for the four seasons
    x = dataset[labels_col] # In these cases, the labels will always be hours
    plot_number = 0
    for col in range(2):
        for row in range(2):
            y = dataset[bars_cols[plot_number]]
            axs[row, col].bar(x, y)
            axs[row, col].set_title(bars_cols[plot_number])
            plot_number += 1
            for i, tick in enumerate(axs[row, col].xaxis.get_major_ticks()):
                if i % 2 != 0:
                    tick.set_visible(False)

    max_ys = []
    for col in bars_cols:
        max_ys.append(max(dataset[col]))

    for i, ax in enumerate(axs.flat):
        if i % 2 == 0:
            ax.set(ylabel=y_label)
        
        if i >= len(axs.flat) - 2:
            ax.set(xlabel=x_label)
        else:
            ax.set_xticks([])
        
        ax.set_ylim([0, 1.05*max(max_ys)])
    
    fig.set_size_inches(12, 10, forward=True)
    
    fig.suptitle(title)

    plt.savefig(destination)
    plt.clf()