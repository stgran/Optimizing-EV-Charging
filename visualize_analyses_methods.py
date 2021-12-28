import matplotlib.pyplot as plt

def seasonal_bars(dataset, bars_cols, labels_col, y_label, x_label, title, destination):
    '''
    This method creates a data visualization containing four barplots (one per season).
    '''
    fig, axs = plt.subplots(2, 2) # We want a 2x2 subplot for the four seasons
    x = dataset[labels_col] # In these cases, the labels will always be hours
    plot_number = 0
    for col in range(2):
        for row in range(2):
            y = dataset[bars_cols[plot_number]] # Gets our seasonal data from the dataset
            axs[row, col].bar(x, y) # Plots a bar plot
            axs[row, col].set_title(bars_cols[plot_number]) # Sets the title as the season
            plot_number += 1
            for i, tick in enumerate(axs[row, col].xaxis.get_major_ticks()):
                if i % 2 != 0:
                    tick.set_visible(False) # We only want to see every other tick label

    # We want the y-axis scales to all be the same so this tracks the max y values for each season.
    max_ys = []
    for col in bars_cols:
        max_ys.append(max(dataset[col]))

    for i, ax in enumerate(axs.flat):
        if i % 2 == 0:
            ax.set(ylabel=y_label) # We only want y-labels on the left-most plots
        
        if i >= len(axs.flat) - 2:
            ax.set(xlabel=x_label) # We only want x-labels on the bottom plots.
        else:
            ax.set_xticks([]) # In the upper plots, we don't want to see x-tick labels.
        
        ax.set_ylim([0, 1.05*max(max_ys)]) # Here, we set the y-axis scale to go to 105% of the max y-value.
    
    fig.set_size_inches(12, 10, forward=True)
    
    fig.suptitle(title) # Titles the plot

    plt.savefig(destination)
    plt.clf() # Clears the plot