def search_matrix(matrix, target):
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // cols][mid % cols]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(search_matrix([[1,3,5],[7,9,11]], 9))
