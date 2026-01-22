def reverseArray(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Example
arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)
print(arr)
