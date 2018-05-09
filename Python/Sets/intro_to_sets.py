def average(array):
    avg_set = set(array)
    return float(sum(avg_set)) / max(len(avg_set), 1)