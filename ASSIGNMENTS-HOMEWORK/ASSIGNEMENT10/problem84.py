def time_to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

def min_time_difference(arr):
    times = [time_to_seconds(t) for t in arr]
    times.sort()
    
    min_diff = float('inf')
    
    for i in range(1, len(times)):
        min_diff = min(min_diff, times[i] - times[i-1])
    
    # circular difference
    min_diff = min(min_diff, 86400 - (times[-1] - times[0]))
    
    return min_diff
