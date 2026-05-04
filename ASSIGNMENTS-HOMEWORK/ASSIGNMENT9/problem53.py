import heapq

def min_operations(arr):
    total = sum(arr)
    target = total / 2
    
    heap = [-x for x in arr]  # max heap
    heapq.heapify(heap)
    
    ops = 0
    curr = total
    
    while curr > target:
        largest = -heapq.heappop(heap)
        half = largest / 2
        
        curr -= half
        heapq.heappush(heap, -half)
        
        ops += 1
    
    return ops
