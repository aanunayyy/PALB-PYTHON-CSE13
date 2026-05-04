def min_people(arr):
    n = len(arr)
    
    intervals = []
    for i in range(n):
        if arr[i] != -1:
            left = max(0, i - arr[i])
            right = min(n - 1, i + arr[i])
            intervals.append((left, right))
    
    intervals.sort()
    
    count = 0
    i = 0
    curr_end = 0
    max_end = 0
    
    while curr_end < n:
        while i < len(intervals) and intervals[i][0] <= curr_end:
            max_end = max(max_end, intervals[i][1])
            i += 1
        
        if max_end == curr_end:
            return -1
        
        count += 1
        curr_end = max_end + 1
    
    return count
