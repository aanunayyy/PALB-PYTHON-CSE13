def row_with_max_ones(matrix):
    max_count = 0
    index = -1

    for i in range(len(matrix)):
        count = sum(matrix[i])
        if count > max_count:
            max_count = count
            index = i

    return index


print(row_with_max_ones([[0,1,1,1],[0,0,1,1],[1,1,1,1]]))
