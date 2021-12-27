def get_daily_var(column):
    max_val = column.max()
    min_val = column.min()
    mean_val = column.mean()
    return (max_val - min_val) / mean_val